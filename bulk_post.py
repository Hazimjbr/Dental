import sys
import os
import time

sys.path.append(os.path.dirname(__file__))
from dental_db import get_channel_last_id, get_channel_post_count
from dental_telegram_bot import post_next_channel_question

def bulk_post_questions(count=30):
    start_id = get_channel_last_id()
    start_post_count = get_channel_post_count()
    print(f"Starting bulk publish. Current Last DB ID: {start_id}, Current Display Count: {start_post_count}")
    print(f"Attempting to publish {count} questions safely...")
    
    success_count = 0
    for i in range(count):
        display_num = post_next_channel_question()
        if display_num:
            success_count += 1
            print(f"Successfully posted channel question #{display_num}")
            # Dynamic sleep to respect Telegram rate limit API (max 30 messages per second, but polls have strict limits)
            time.sleep(2)
        else:
            print("Failed to post question. Rate limit handler will retry on next attempts.")
            time.sleep(5)
            
    print(f"Bulk publish completed. Successfully posted {success_count} questions.")

if __name__ == '__main__':
    # Default to posting 30 questions
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=30)
    args = parser.parse_args()
    
    bulk_post_questions(args.count)
