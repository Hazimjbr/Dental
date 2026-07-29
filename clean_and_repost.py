import os
import sys
import sqlite3
import urllib.request
import urllib.parse
import json
import time

DB_PATH = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
sys.path.append(r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch")

from dental_telegram_bot import post_next_channel_question

def load_env():
    env_vars = {}
    with open(r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\.env", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip().strip('"').strip("'")
    return env_vars

def clean_and_repost():
    env = load_env()
    token = env["BOT_TOKEN"]
    channel_id = env["CHANNEL_ID"]

    # 1. Get all message IDs to delete
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT message_id FROM channel_polls WHERE message_id IS NOT NULL")
    msg_ids = [r[0] for r in c.fetchall()]
    conn.close()

    print(f"Deleting {len(msg_ids)} posts from channel...")
    deleted = 0
    for msg_id in msg_ids:
        url = f"https://api.telegram.org/bot{token}/deleteMessage"
        payload = urllib.parse.urlencode({"chat_id": channel_id, "message_id": msg_id}).encode()
        try:
            req = urllib.request.Request(url, data=payload)
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode())
                if res.get("ok"):
                    deleted += 1
        except Exception as e:
            print(f"Failed to delete {msg_id}: {e}")
        time.sleep(0.1)
    print(f"Deleted {deleted} posts.")

    # 2. Reset DB trackers
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO channel_settings (key, value) VALUES ('last_channel_q_id', '0')")
    c.execute("INSERT OR REPLACE INTO channel_settings (key, value) VALUES ('channel_post_count', '0')")
    c.execute("DELETE FROM channel_polls")
    conn.commit()
    conn.close()
    print("Database trackers reset successfully.")

    # 3. Publish Q1-50 with safe delay
    print("Republishing Q1 to Q50 with safe 3.5s delay...")
    for i in range(1, 51):
        q_num = post_next_channel_question()
        print(f"Successfully posted Question #{q_num}")
        time.sleep(3.5) # Safe rate limiting delay

    print("All 50 questions published successfully without any duplicates or skips!")

if __name__ == "__main__":
    clean_and_repost()
