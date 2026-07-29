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

def fix_explanations_and_repost():
    env = load_env()
    token = env["BOT_TOKEN"]
    channel_id = env["CHANNEL_ID"]

    # 1. Update Database IDs 201 to 211
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    q201_211_exps = {
        201: 'Hypertonic fluids draw fluid out of the dentinal tubules (from inside to outside) via osmotic pressure, stimulating nociceptors.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
        202: 'Fluid movement in dentinal tubules in response to osmotic, thermal, or mechanical stimuli is explained by Brännström\'s Hydrodynamic Theory.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
        204: 'Angioedema presents with rapid, painless swelling of the soft tissues (like lips or eyes) without any odontogenic infection.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
        205: 'The reducing zone (center of the flame) is used for melting gold alloys to prevent oxidation during casting.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 129)',
        206: 'Placing the occlusal plane slightly below the dorsum of the tongue allows the tongue to rest on the denture, increasing stability.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
        207: 'Rapid heating during burnout causes steam formation and rapid expansion, leading to cracking of the investment mold.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 128)',
        208: 'Gypsum dies have relatively low edge strength and can easily chip or lose fine surface details during carving or handling.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 132)',
        210: 'When the electrosurgery current intensity is set too low, the electrode drags and tissue coagulates/sticks to the tip.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 80)',
        211: 'Hybrid composites incorporate submicron glass particles (microfilled elements) providing high wear resistance for posterior stress-bearing areas.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)'
    }

    for q_id, exp in q201_211_exps.items():
        c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))
    conn.commit()
    print("Database IDs 201-211 enriched successfully.")

    # 2. Get message IDs to delete for display #192 to #200 (database IDs 201 to 211)
    c.execute("SELECT message_id, display_num FROM channel_polls WHERE display_num BETWEEN 192 AND 200")
    rows = c.fetchall()
    
    print(f"Deleting {len(rows)} posts (numbers 192-200) from channel...")
    deleted = 0
    for message_id, display_num in rows:
        if message_id:
            url = f"https://api.telegram.org/bot{token}/deleteMessage"
            payload = urllib.parse.urlencode({"chat_id": channel_id, "message_id": message_id}).encode()
            try:
                req = urllib.request.Request(url, data=payload)
                with urllib.request.urlopen(req) as resp:
                    res = json.loads(resp.read().decode())
                    if res.get("ok"):
                        deleted += 1
            except Exception as e:
                print(f"Failed to delete display #{display_num} (msg_id {message_id}): {e}")
            time.sleep(0.1)
    print(f"Deleted {deleted} posts from channel.")

    # Remove deleted from mapping table
    c.execute("DELETE FROM channel_polls WHERE display_num BETWEEN 192 AND 200")
    
    # 3. Reset settings to pre-192 state: Display count = 191, last question ID = 199 (since ID 199 was displayed as #191)
    c.execute("INSERT OR REPLACE INTO channel_settings (key, value) VALUES ('last_channel_q_id', '199')")
    c.execute("INSERT OR REPLACE INTO channel_settings (key, value) VALUES ('channel_post_count', '191')")
    conn.commit()
    conn.close()
    print("Trackers reset to #191 successfully.")

    # 4. Post Q192 to Q200 cleanly
    print("Republishing Q192 to Q200 with proper explanations...")
    for i in range(192, 201):
        q_num = post_next_channel_question()
        print(f"Successfully posted Question #{q_num}")
        time.sleep(3.5)

    print("Fix and republication of Q192-200 completed successfully!")

if __name__ == "__main__":
    fix_explanations_and_repost()
