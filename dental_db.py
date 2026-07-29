import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'dental_bot.db')
QUESTIONS_JSON = os.path.join(os.path.dirname(__file__), 'full_1000_mcqs.json')

def categorize_question(q_text):
    text_lower = q_text.lower()
    if any(k in text_lower for k in ['nerve', 'abscess', 'surgery', 'extraction', 'flap', 'sinus', 'fracture', 'trauma', 'suture', 'lesion', 'carcinoma']):
        return "Oral Surgery & Pathology"
    elif any(k in text_lower for k in ['canal', 'pulp', 'endodontic', 'amalgam', 'gic', 'composite', 'cavity', 'caries', 'dentin', 'enamel']):
        return "Restorative & Endodontics"
    elif any(k in text_lower for k in ['periodontal', 'gingival', 'calculus', 'pocket', 'plaque', 'hygiene', 'scaling']):
        return "Periodontics"
    elif any(k in text_lower for k in ['denture', 'impression', 'crown', 'bridge', 'x-ray', 'radiograph', 'cast', 'occlusion', 'abutment']):
        return "Prosthodontics & Radiology"
    elif any(k in text_lower for k in ['penicillin', 'diazepam', 'sedation', 'fluoride', 'anaesthesia', 'drug', 'antibiotic', 'steroid', 'cirrhosis']):
        return "Pharmacology & General Medicine"
    else:
        return "General Dentistry"

def calculate_difficulty_level(q_text, options_list):
    text_len = len(q_text)
    text_lower = q_text.lower()
    num_options = len(options_list) if isinstance(options_list, list) else 4
    
    complexity_keywords = ['emergency', 'management', 'contraindicated', 'diagnose', 'syndrome', 'carcinoma', 'pathognomonic', 'complication']
    
    if num_options >= 5 or text_len > 180 or any(k in text_lower for k in complexity_keywords):
        return "Level 3"
    elif text_len < 90 and num_options <= 4:
        return "Level 1"
    else:
        return "Level 2"

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
    
    # 6. Persistent Channel Polls Mapping Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS channel_polls (
        poll_id TEXT PRIMARY KEY,
        question_id INTEGER,
        display_num INTEGER,
        message_id INTEGER,
        correct_option_id INTEGER,
        comment_posted INTEGER DEFAULT 0
    )
    ''')
    
    # 7. Weekly stats Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weekly_stats (
        user_id INTEGER,
        week_start TEXT,
        total_answered INTEGER DEFAULT 0,
        correct_answers INTEGER DEFAULT 0,
        PRIMARY KEY (user_id, week_start)
    )
    ''')
    
    # 8. Pearls Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pearls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pearl_text TEXT NOT NULL,
        category TEXT,
        reference TEXT,
        posted INTEGER DEFAULT 0
    )
    ''')
    
    # 9. Exam dates Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exam_dates (
        user_id INTEGER PRIMARY KEY,
        exam_type TEXT,
        exam_date TEXT
    )
    ''')
    
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM questions')
    if cursor.fetchone()[0] == 0:
        if os.path.exists(QUESTIONS_JSON):
            with open(QUESTIONS_JSON, 'r', encoding='utf-8') as f:
                qs = json.load(f)
            
            records = []
            for q in qs:
                cat = categorize_question(q['question'])
                lvl = calculate_difficulty_level(q['question'], q['options'])
                corr_idx = q['correct_option_id'] if q['correct_option_id'] is not None else 0
                records.append((
                    q['id'],
                    q['question'],
                    json.dumps(q['options'], ensure_ascii=False),
                    q.get('correct_letter', 'A'),
                    corr_idx,
                    q.get('explanation', ''),
                    cat,
                    lvl
                ))
            
            cursor.executemany('''
            INSERT INTO questions (id, question, options_json, correct_letter, correct_option_id, explanation, category, level)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', records)
            conn.commit()

    conn.close()

def save_channel_poll_mapping(poll_id, question_id, display_num, message_id, correct_option_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO channel_polls (poll_id, question_id, display_num, message_id, correct_option_id, comment_posted)
    VALUES (?, ?, ?, ?, ?, 0)
    ''', (str(poll_id), question_id, display_num, message_id, correct_option_id))
    conn.commit()
    conn.close()

def get_channel_poll_mapping(poll_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT poll_id, question_id, display_num, message_id, correct_option_id, comment_posted FROM channel_polls WHERE poll_id = ?', (str(poll_id),))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'poll_id': row[0],
            'question_id': row[1],
            'display_num': row[2],
            'message_id': row[3],
            'correct_option_id': row[4],
            'comment_posted': row[5]
        }
    return None

def mark_channel_poll_comment_posted(poll_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE channel_polls SET comment_posted = 1 WHERE poll_id = ?', (str(poll_id),))
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

if __name__ == '__main__':
    init_db()
    print("Database functions loaded with Persistent Channel Polls table.")
