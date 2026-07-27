# Dental Telegram Quiz Bot Script
import json
import urllib.request
import urllib.parse
import time
import os

BOT_TOKEN = "8889900356:AAEyNXWF_glSMSukdA59-xHgbwd6BcQvdbg"

def load_questions():
    json_path = os.path.join(os.path.dirname(__file__), 'full_1000_mcqs.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def send_quiz_poll(bot_token, chat_id, question_data):
    """
    Sends a native Telegram Quiz Poll with Question, Options, Correct Answer,
    and a built-in Explanation pop-up.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendPoll"
    
    question_text = f"Q#{question_data['id']}: {question_data['question']}"[:300]
    options = [opt[:100] for opt in question_data['options'][:10]]
    correct_id = question_data['correct_option_id'] if question_data['correct_option_id'] is not None else 0
    
    corr_letter = question_data.get('correct_letter', 'A')
    raw_exp = question_data.get('explanation', '')
    
    if raw_exp:
        exp_text = f"Correct: ({corr_letter}). {raw_exp}"[:200]
    else:
        exp_text = f"Correct Answer: ({corr_letter}). Reference: Master Dentistry Vol 1 & 2."[:200]

    payload = {
        'chat_id': chat_id,
        'question': question_text,
        'options': json.dumps(options),
        'type': 'quiz',
        'correct_option_id': correct_id,
        'explanation': exp_text,
        'is_anonymous': False
    }
    
    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get('ok'):
                print(f" Successfully posted Question #{question_data['id']} to {chat_id}!")
            else:
                print(" API Error:", res)
            return res
    except Exception as e:
        print(" Error sending quiz poll:", e)
        return None

if __name__ == '__main__':
    print(" Telegram Dental Quiz Bot Connected!")
    questions = load_questions()
    print(f" Loaded {len(questions)} questions.")
