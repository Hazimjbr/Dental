import time
import os
import sqlite3
import datetime
import urllib.request
import urllib.parse
import json
import random

from dental_db import DB_PATH, get_all_exam_dates
from pearls_content import PEARLS

# Helper to read .env file line by line
def load_env():
    env_vars = {}
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        key, value = parts
                        env_vars[key.strip()] = value.strip().strip('"').strip("'")
    return env_vars

# Load secrets
env = load_env()
BOT_TOKEN = env.get("BOT_TOKEN", "")
CHANNEL_ID = env.get("CHANNEL_ID", "@dentistry_mcqs_2026")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def api_call(method, payload=None):
    url = f"{API_URL}/{method}"
    data = None
    if payload:
        data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Scheduler API Error [{method}]:", e)
        return None

def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    return api_call('sendMessage', payload)

def post_daily_pearl():
    pearl = random.choice(PEARLS)
    pearl_text = (
        f"💎 <b>Daily Clinical Pearl</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{pearl['text']}\n\n"
        f"📚 <b>Category:</b> #{pearl['category'].replace(' & ', '_').replace(' ', '_')}\n"
        f"🏛️ <b>Reference:</b> {pearl['reference']}"
    )
    send_message(CHANNEL_ID, pearl_text)
    print("Posted daily clinical pearl to channel.")

def post_exam_countdown():
    dates = get_all_exam_dates()
    if not dates:
        return
        
    today = datetime.date.today()
    for user_id, exam_type, date_str in dates:
        try:
            exam_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            days_left = (exam_date - today).days
            if days_left >= 0:
                msg = (
                    f"📅 <b>Exam Countdown Update</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"🎯 <b>Exam Target:</b> {exam_type}\n"
                    f"🗓️ <b>Days Remaining:</b> {days_left} Days\n\n"
                    f"Stay focused and practice your Level 3 questions today! 💪"
                )
                send_message(user_id, msg)
        except Exception as e:
            print("Error in countdown for user:", user_id, e)

def send_weekly_reports():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    today = datetime.date.today()
    week_start = (today - datetime.timedelta(days=today.weekday())).strftime('%Y-%m-%d')
    
    cursor.execute('''
        SELECT u.user_id, u.first_name, ws.total_answered, ws.correct_answers
        FROM users u
        JOIN weekly_stats ws ON u.user_id = ws.user_id
        WHERE ws.week_start = ?
    ''', (week_start,))
    rows = cursor.fetchall()
    conn.close()
    
    for user_id, name, total, correct in rows:
        accuracy = (correct / total * 100) if total > 0 else 0
        report_msg = (
            f"📊 <b>Weekly Progress Report — Dr. {name}</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"✅ <b>Questions Solved This Week:</b> {total}\n"
            f"🎯 <b>Weekly Accuracy Rate:</b> {accuracy:.1f}%\n\n"
            f"🏆 Keep up the daily practice to improve your board scores!"
        )
        send_message(user_id, report_msg)
    print("Sent weekly progress reports to active users.")

def start_scheduler():
    print("Dental Scheduler Engine Started.")
    
    last_pearl_day = None
    last_weekly_report = None
    
    while True:
        now = datetime.datetime.now()
        
        if now.hour == 9 and now.minute == 0 and last_pearl_day != now.date():
            post_daily_pearl()
            post_exam_countdown()
            last_pearl_day = now.date()
            
        if now.weekday() == 0 and now.hour == 8 and now.minute == 0 and last_weekly_report != now.date():
            send_weekly_reports()
            last_weekly_report = now.date()
            
        time.sleep(30)

if __name__ == '__main__':
    start_scheduler()
