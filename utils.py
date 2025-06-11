import re
from difflib import get_close_matches
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

def match_faq(message, faq_dict):
    for pattern, response in faq_dict.items():
        if re.search(pattern, message, re.IGNORECASE):
            return response

    for pattern in faq_dict:
        words = re.findall(r'\\b\\w+\\b', pattern)
        match = get_close_matches(message.lower(), words, n=1, cutoff=0.8)
        if match:
            return faq_dict[pattern]

    return None

def log_question(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/questions.log", "a") as log:
        log.write(f"[{datetime.now()}] {message}\\n")

def notify_unanswered(message):
    try:
        msg = EmailMessage()
        msg.set_content(f"Unanswered question received: {message}")
        msg['Subject'] = 'New Unanswered Chatbot Question'
        msg['From'] = os.getenv('EMAIL_USER')
        msg['To'] = os.getenv('EMAIL_TO')

        with smtplib.SMTP(os.getenv('EMAIL_SERVER'), int(os.getenv('EMAIL_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.send_message(msg)
    except Exception as e:
        print(f"Notification failed: {e}")