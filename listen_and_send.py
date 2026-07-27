import urllib.request
import urllib.parse
import json
import time
import os

token = '8889900356:AAEyNXWF_glSMSukdA59-xHgbwd6BcQvdbg'
json_path = os.path.join(os.path.dirname(__file__), 'full_1000_mcqs.json')

with open(json_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

q1 = questions[0]
url_updates = f'https://api.telegram.org/bot{token}/getUpdates'

print("Waiting for user to click Start on @dentistry_quiz_bot...")
start_time = time.time()
offset = 0

while time.time() - start_time < 30:
    try:
        req_url = f"{url_updates}?offset={offset}"
        with urllib.request.urlopen(req_url) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            results = res.get('result', [])
            for item in results:
                offset = item['update_id'] + 1
                if 'message' in item:
                    chat_id = item['message']['chat']['id']
                    first_name = item['message']['chat'].get('first_name', 'Doctor')
                    print(f"Detected user {first_name} (chat_id: {chat_id})!")
                    
                    # Send Quiz Poll
                    url_poll = f"https://api.telegram.org/bot{token}/sendPoll"
                    explanation = "💡 Correct: (A). In lower premolars, handpiece is inclined lingually to avoid damaging the larger buccal pulp horn and conserve tooth structure."
                    
                    payload = {
                        'chat_id': chat_id,
                        'question': f"Q#1: {q1['question']}"[:300],
                        'options': json.dumps([opt[:100] for opt in q1['options']]),
                        'type': 'quiz',
                        'correct_option_id': q1['correct_option_id'] if q1['correct_option_id'] is not None else 0,
                        'explanation': explanation,
                        'is_anonymous': False
                    }
                    
                    data = urllib.parse.urlencode(payload).encode('utf-8')
                    req = urllib.request.Request(url_poll, data=data)
                    with urllib.request.urlopen(req) as p_resp:
                        p_res = json.loads(p_resp.read().decode('utf-8'))
                        print("Poll sent status:", p_res.get('ok'))
                    break
    except Exception as e:
        print("Polling error:", e)
    time.sleep(2)
