import urllib.request
import urllib.parse
import json
import time
import os
import sqlite3
import random
import re
from dental_db import (
    init_db, get_user, update_user_progress, log_user_answer,
    get_question_by_id, get_next_question, get_pending_mistakes, search_questions,
    get_channel_last_id, update_channel_last_id, get_next_available_id,
    get_channel_post_count, increment_channel_post_count, reset_channel_post_count
)

# Helper to read .env file line by line without external dependencies
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

def get_formatted_category_header(category):
    cat_map = {
        "Oral Surgery & Pathology": "🔪 #Oral_Surgery",
        "Restorative & Endodontics": "🦷 #Endodontics",
        "Periodontics": "🩺 #Periodontics",
        "Prosthodontics & Radiology": "📸 #Prosthodontics",
        "Pharmacology & General Medicine": "💊 #Pharmacology",
        "General Dentistry": "✨ #General_Dentistry"
    }
    return cat_map.get(category, "✨ #Dentistry")

def get_level_badge(level):
    lvl_map = {
        "Level 1": "🟢 Level 1",
        "Level 2": "🟡 Level 2",
        "Level 3": "🔴 Level 3"
    }
    return lvl_map.get(level, "🟡 Level 2")

def api_call(method, payload=None):
    url = f"{API_URL}/{method}"
    data = None
    if payload:
        data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("Rate limit hit (429). Sleeping 10 seconds...")
                time.sleep(10)
                continue
            else:
                print(f"API Error [{method}]:", e)
                return None
        except Exception as e:
            print(f"API Connection Error [{method}]:", e)
            return None
    return None

def send_message(chat_id, text, reply_markup=None, reply_to_message_id=None, parse_mode='HTML'):
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    if reply_markup:
        payload['reply_markup'] = json.dumps(reply_markup)
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    return api_call('sendMessage', payload)

def answer_callback_query(callback_query_id, text, show_alert=True):
    payload = {
        'callback_query_id': callback_query_id,
        'text': text,
        'show_alert': show_alert
    }
    return api_call('answerCallbackQuery', payload)

def send_inline_quiz(chat_id, question_data, display_num=None):
    category = question_data.get('category', 'General Dentistry')
    level = question_data.get('level', 'Level 2')
    
    cat_header = get_formatted_category_header(category)
    lvl_badge = get_level_badge(level)
    
    num = display_num if display_num is not None else question_data['id']
    
    original_options = list(question_data['options'])
    correct_idx = question_data['correct_option_id'] if question_data['correct_option_id'] is not None else 0
    if correct_idx >= len(original_options):
        correct_idx = 0
        
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    
    formatted_opts_lines = []
    inline_buttons = []
    row = []
    
    for idx, opt in enumerate(original_options):
        let = letters[idx] if idx < len(letters) else str(idx+1)
        formatted_opts_lines.append(f"<b>{let})</b> {opt}")
        row.append({
            'text': f" Option {let} ",
            'callback_data': f"quiz:{question_data['id']}:{idx}:{correct_idx}"
        })
        if len(row) == 2:
            inline_buttons.append(row)
            row = []
    if row:
        inline_buttons.append(row)
        
    opts_block = "\n".join(formatted_opts_lines)
    msg_text = (
        f"❓ <b>Question #{num}</b>  |  {lvl_badge}  |  {cat_header}\n\n"
        f"{question_data['question']}\n\n"
        f"{opts_block}\n\n"
        f"👇 <i>Tap an option below to vote and reveal the clinical explanation:</i>"
    )
    
    reply_markup = {'inline_keyboard': inline_buttons}
    return send_message(chat_id, msg_text, reply_markup=reply_markup, parse_mode='HTML')

def post_next_channel_question():
    last_id = get_channel_last_id()
    next_id = get_next_available_id(last_id)
    q = get_question_by_id(next_id)
    
    next_display = get_channel_post_count() + 1
    
    res = send_inline_quiz(CHANNEL_ID, q, display_num=next_display)
    if res and res.get('ok'):
        increment_channel_post_count()
        update_channel_last_id(next_id)
        print(f" Successfully posted Inline Button Quiz #{next_id} (Displayed as #{next_display}) to {CHANNEL_ID}")
        return next_display
    return None

def get_main_keyboard():
    return {
        'keyboard': [
            [{'text': '🎯 Next Question'}, {'text': '🔴 My Mistakes'}],
            [{'text': '🏷️ Specialties'}, {'text': '📊 My Progress'}],
            [{'text': '🔍 Search MCQs'}, {'text': '📢 Official Channel'}]
        ],
        'resize_keyboard': True
    }

def handle_start(chat_id, user_id, first_name, username):
    get_user(user_id, username, first_name)
    welcome_text = (
        f"🦷 <b>Welcome Dr. {first_name} to Dental MCQs Platform!</b>\n\n"
        f"Designed to help you master board exams (ORE, MFDs, MJDF) efficiently.\n\n"
        f"📌 <b>Platform Features:</b>\n"
        f"• 🎯 <b>910 Board Questions</b> categorized with PubMed & Book references.\n"
        f"• 🔴 <b>Mistakes Deck:</b> Auto-saves missed questions for targeted review.\n"
        f"• 🏷️ <b>Specialties & Levels:</b> Filter by subject and difficulty.\n"
        f"• ⏩ <b>Progress Tracking:</b> Automatically resumes from where you left off.\n"
        f"• 📢 <b>Official Channel:</b> {CHANNEL_ID}\n\n"
        f"Select an option below to start practicing 👇"
    )
    send_message(chat_id, welcome_text, reply_markup=get_main_keyboard())

def handle_next_quiz(chat_id, user_id):
    q = get_next_question(user_id)
    if q:
        send_inline_quiz(chat_id, q)
        update_user_progress(user_id, q['id'])
    else:
        send_message(chat_id, "🎉 Congratulations! You have completed all available questions!")

def handle_mistakes(chat_id, user_id):
    mistakes = get_pending_mistakes(user_id)
    if not mistakes:
        send_message(chat_id, "🌟 <b>Excellent!</b> You currently have no pending mistakes in your review deck.")
    else:
        q = mistakes[0]
        send_message(chat_id, "🔴 <b>Reviewing Mistakes:</b>")
        send_inline_quiz(chat_id, q)

def handle_categories_menu(chat_id):
    cats_text = (
        "🏷️ <b>Available Dental Specialties & Hashtags:</b>\n\n"
        "1️⃣ 🔪 <b>Oral Surgery & Pathology</b> (<code>#Oral_Surgery</code>)\n"
        "2️⃣ 🦷 <b>Restorative & Endodontics</b> (<code>#Endodontics</code>)\n"
        "3️⃣ 🩺 <b>Periodontics</b> (<code>#Periodontics</code>)\n"
        "4️⃣ 📸 <b>Prosthodontics & Radiology</b> (<code>#Prosthodontics</code>)\n"
        "5️⃣ 💊 <b>Pharmacology & Medicine</b> (<code>#Pharmacology</code>)\n\n"
        "💡 <b>Tip:</b> In the channel, tap any hashtag to view all questions for that sub-specialty instantly!"
    )
    send_message(chat_id, cats_text)

def handle_stats(chat_id, user_id, first_name):
    user = get_user(user_id)
    last_q_id = user[3]
    total_ans = user[4]
    correct_ans = user[5]
    accuracy = (correct_ans / total_ans * 100) if total_ans > 0 else 0
    mistakes_count = len(get_pending_mistakes(user_id))
    
    stats_text = (
        f"📊 <b>Progress Dashboard for Dr. {first_name}:</b>\n\n"
        f"📍 <b>Last Question Reached:</b> #{last_q_id} / 910\n"
        f"📝 <b>Total Questions Answered:</b> {total_ans}\n"
        f"✅ <b>Correct Answers:</b> {correct_ans}\n"
        f"🎯 <b>Accuracy Rate:</b> {accuracy:.1f}%\n"
        f"🔴 <b>Pending Mistakes:</b> {mistakes_count}\n\n"
        f"Keep practicing daily to build your exam readiness! 💪"
    )
    send_message(chat_id, stats_text)

def handle_search_prompt(chat_id):
    send_message(chat_id, "🔍 <b>Search Dental MCQs Database:</b>\nType <code>/search</code> followed by your keyword.\nExample:\n<code>/search amalgam</code>\n<code>/search GIC</code>\n<code>/search nerve</code>")

def execute_search(chat_id, query):
    results = search_questions(query, limit=3)
    if not results:
        send_message(chat_id, f"❌ No questions found matching: <code>{query}</code>")
    else:
        send_message(chat_id, f"🔍 <b>Search Results for ({query}):</b>")
        for q in results:
            send_inline_quiz(chat_id, q)

def handle_channel_info(chat_id):
    info = (
        f"📢 <b>Official Dental Board Practice Channel:</b>\n{CHANNEL_ID}\n\n"
        f"Interactive quizzes with clinical explanations are posted daily!\n"
        f"👉 <a href=\"https://t.me/dentistry_quiz_bot\">Click here to launch Private Practice Bot</a>"
    )
    send_message(chat_id, info)

def run_bot():
    init_db()
    print("Dental Telegram Quiz Bot is NOW LIVE (Inline Buttons Mandatory Alert Popup)!")
    offset = 0
    
    while True:
        try:
            res = api_call('getUpdates', {'offset': offset, 'timeout': 10})
            if res and res.get('ok'):
                for update in res.get('result', []):
                    offset = update['update_id'] + 1
                    
                    if 'callback_query' in update:
                        cq = update['callback_query']
                        cq_id = cq['id']
                        u_id = cq['from']['id']
                        data = cq.get('data', '')
                        
                        if data.startswith('quiz:'):
                            parts = data.split(':')
                            q_id = int(parts[1])
                            chosen_idx = int(parts[2])
                            corr_idx = int(parts[3])
                            
                            is_corr = (chosen_idx == corr_idx)
                            log_user_answer(u_id, q_id, chosen_idx, is_corr)
                            
                            q_data = get_question_by_id(q_id)
                            if q_data:
                                corr_text = q_data['options'][corr_idx] if corr_idx < len(q_data['options']) else ""
                                status_head = "✅ CORRECT ANSWER!" if is_corr else "❌ INCORRECT ANSWER!"
                                
                                alert_msg = (
                                    f"{status_head}\n"
                                    f"🎯 Choice: {corr_text}\n\n"
                                    f"{q_data['explanation']}"
                                )
                                # Forces popup alert on student screen in 100% of cases (RIGHT OR WRONG)!
                                answer_callback_query(cq_id, alert_msg[:195], show_alert=True)
                    
                    if 'message' in update and 'text' in update['message']:
                        msg = update['message']
                        c_id = msg['chat']['id']
                        u_id = msg['from']['id']
                        f_name = msg['from'].get('first_name', 'Doctor')
                        u_name = msg['from'].get('username', '')
                        text = msg['text'].strip()
                        
                        if text == '/start':
                            handle_start(c_id, u_id, f_name, u_name)
                        elif text in ['🎯 Next Question', '/quiz']:
                            handle_next_quiz(c_id, u_id)
                        elif text in ['🔴 My Mistakes', '/mistakes']:
                            handle_mistakes(c_id, u_id)
                        elif text in ['🏷️ Specialties', '/categories']:
                            handle_categories_menu(c_id)
                        elif text in ['📊 My Progress', '/stats']:
                            handle_stats(c_id, u_id, f_name)
                        elif text in ['🔍 Search MCQs']:
                            handle_search_prompt(c_id)
                        elif text.startswith('/search'):
                            parts = text.split(maxsplit=1)
                            if len(parts) > 1:
                                execute_search(c_id, parts[1])
                            else:
                                handle_search_prompt(c_id)
                        elif text in ['📢 Official Channel', '/channel']:
                            handle_channel_info(c_id)
                        elif text == '/post':
                            posted_id = post_next_channel_question()
                            if posted_id:
                                send_message(c_id, f"✅ Question #{posted_id} posted successfully to {CHANNEL_ID}!")
                            else:
                                send_message(c_id, "❌ Error posting to channel.")
                        else:
                            handle_next_quiz(c_id, u_id)
        except Exception as e:
            print("Loop error:", e)
        time.sleep(1)

if __name__ == '__main__':
    run_bot()
