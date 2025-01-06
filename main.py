# main.py
"""
Entry point of ColdContactXLSX.
"""

import logging
import email_utils.follow_up as follow_up
import sys
from gui import main as gui_main

from scheduler.schedule_now import send_emails_now
from scheduler.send_later import schedule_emails

# Set up logging with debug option
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    choice = input("Is this the first email or a follow-up? (first/follow-up): ").lower()

    if choice == 'first':
        first_email_flow()
    elif choice == 'follow-up':
        follow_up_flow()
    else:
        print("Invalid choice. Please enter 'first' or 'follow-up'.")

def first_email_flow():
    choice = input("Do you want to send the email now or schedule it for a specific time? (now/schedule): ").lower()

    if choice == 'now':
        send_emails_now()
    elif choice == 'schedule':
        schedule_emails()
    else:
        print("Invalid choice. Please enter 'now' or 'schedule'.")

def follow_up_flow():
    follow_up.send_follow_up_email()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        from cli import main as cli_main
        cli_main()
    else:
        gui_main()
