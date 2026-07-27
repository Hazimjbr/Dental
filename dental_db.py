import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'dental_bot.db')
QUESTIONS_JSON = os.path.join(os.path.dirname(__file__), 'full_1000_mcqs.json')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Questions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        options_json TEXT NOT NULL,
        correct_letter TEXT,
        correct_option_id INTEGER,
        explanation TEXT,
        category TEXT,
        level TEXT DEFAULT 'Level 2'
    )
    ''')
    
    # 2. Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_question_id INTEGER DEFAULT 0,
        total_answered INTEGER DEFAULT 0,
        correct_answers INTEGER DEFAULT 0,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 3. User Answers Log Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_id INTEGER,
        chosen_option_id INTEGER,
        is_correct INTEGER,
        answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 4. User Mistakes Bank Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_mistakes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_id INTEGER,
        status TEXT DEFAULT 'pending',
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, question_id)
    )
    ''')
    
    # 5. Channel settings Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS channel_settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')
    cursor.execute('INSERT OR IGNORE INTO channel_settings (key, value) VALUES ("last_channel_q_id", "0")')
    cursor.execute('INSERT OR IGNORE INTO channel_settings (key, value) VALUES ("channel_post_count", "0")')
    conn.commit()
    conn.close()

def get_channel_last_id():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM channel_settings WHERE key = "last_channel_q_id"')
    row = cursor.fetchone()
    conn.close()
    return int(row[0]) if row else 0

def update_channel_last_id(q_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO channel_settings (key, value) VALUES ("last_channel_q_id", ?)', (str(q_id),))
    conn.commit()
    conn.close()

def get_channel_post_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM channel_settings WHERE key = "channel_post_count"')
    row = cursor.fetchone()
    conn.close()
    return int(row[0]) if row else 0

def increment_channel_post_count():
    current = get_channel_post_count()
    new_count = current + 1
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO channel_settings (key, value) VALUES ("channel_post_count", ?)', (str(new_count),))
    conn.commit()
    conn.close()
    return new_count

def reset_channel_post_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO channel_settings (key, value) VALUES ("channel_post_count", "0")', ())
    conn.commit()
    conn.close()

def get_next_available_id(last_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM questions WHERE id > ? ORDER BY id ASC LIMIT 1', (last_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    
    # Loop back to absolute first question in DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM questions ORDER BY id ASC LIMIT 1')
    first_row = cursor.fetchone()
    conn.close()
    return first_row[0] if first_row else 1

def get_user(user_id, username='', first_name=''):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute('INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?)', (user_id, username, first_name))
        conn.commit()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
    conn.close()
    return row

def update_user_progress(user_id, last_q_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET last_question_id = ? WHERE user_id = ?', (last_q_id, user_id))
    conn.commit()
    conn.close()

def log_user_answer(user_id, question_id, chosen_idx, is_correct):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_answers (user_id, question_id, chosen_option_id, is_correct) VALUES (?, ?, ?, ?)',
                   (user_id, question_id, chosen_idx, 1 if is_correct else 0))
    cursor.execute('''
    UPDATE users 
    SET total_answered = total_answered + 1,
        correct_answers = correct_answers + ?
    WHERE user_id = ?
    ''', (1 if is_correct else 0, user_id))
    
    import datetime
    today = datetime.date.today()
    week_start = (today - datetime.timedelta(days=today.weekday())).strftime('%Y-%m-%d')
    cursor.execute('''
    INSERT INTO weekly_stats (user_id, week_start, total_answered, correct_answers)
    VALUES (?, ?, 1, ?)
    ON CONFLICT(user_id, week_start) DO UPDATE SET
        total_answered = total_answered + 1,
        correct_answers = correct_answers + excluded.correct_answers
    ''', (user_id, week_start, 1 if is_correct else 0))
    
    if not is_correct:
        cursor.execute('INSERT OR IGNORE INTO user_mistakes (user_id, question_id, status) VALUES (?, ?, "pending")',
                       (user_id, question_id))
    else:
        cursor.execute('UPDATE user_mistakes SET status = "resolved" WHERE user_id = ? AND question_id = ?',
                       (user_id, question_id))
        
    conn.commit()
    conn.close()

def get_question_by_id(q_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, question, options_json, correct_letter, correct_option_id, explanation, category, level FROM questions WHERE id = ?', (q_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'question': row[1],
            'options': json.loads(row[2]),
            'correct_letter': row[3],
            'correct_option_id': row[4],
            'explanation': row[5],
            'category': row[6],
            'level': row[7] if len(row) > 7 and row[7] else "Level 2"
        }
    return None

def get_next_question(user_id):
    user = get_user(user_id)
    last_id = user[3]
    next_id = get_next_available_id(last_id)
    return get_question_by_id(next_id)

def get_pending_mistakes(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT q.id, q.question, q.options_json, q.correct_letter, q.correct_option_id, q.explanation, q.category, q.level
    FROM user_mistakes m
    JOIN questions q ON m.question_id = q.id
    WHERE m.user_id = ? AND m.status = 'pending'
    ''', (user_id,))
    rows = cursor.fetchall()
    conn.close()
    
    mistakes = []
    for row in rows:
        mistakes.append({
            'id': row[0],
            'question': row[1],
            'options': json.loads(row[2]),
            'correct_letter': row[3],
            'correct_option_id': row[4],
            'explanation': row[5],
            'category': row[6],
            'level': row[7] if len(row) > 7 and row[7] else "Level 2"
        })
    return mistakes

def search_questions(keyword, limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, question, options_json, correct_letter, correct_option_id, explanation, category, level FROM questions WHERE question LIKE ? OR explanation LIKE ? LIMIT ?',
                   (f'%{keyword}%', f'%{keyword}%', limit))
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            'id': row[0],
            'question': row[1],
            'options': json.loads(row[2]),
            'correct_letter': row[3],
            'correct_option_id': row[4],
            'explanation': row[5],
            'category': row[6],
            'level': row[7] if len(row) > 7 and row[7] else "Level 2"
        })
    return results

def set_exam_date(user_id, exam_type, exam_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO exam_dates (user_id, exam_type, exam_date) VALUES (?, ?, ?)',
                   (user_id, exam_type, exam_date))
    conn.commit()
    conn.close()

def get_exam_date(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT exam_type, exam_date FROM exam_dates WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_exam_dates():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, exam_type, exam_date FROM exam_dates')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    init_db()
    print("Database functions corrected with display count.")
