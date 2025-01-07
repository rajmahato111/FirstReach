# email_utils/email_sender.py
"""
Module to handle sending emails.
"""

import os
import logging
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr  # Add this import

resume_filename = "Raj_SDE_Resume.pdf"  # Update as necessary
resume_path = os.path.join("email_assets", resume_filename)

# Set up logging
logger = logging.getLogger(__name__)

def send_email(sender_email, password, recipient_email, subject, html_content, company_name):
    """
    Sends an email with an attachment.
    
    Args:
        sender_email (str): Sender's email address.
        password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Email subject.
        html_content (str): Email body message in HTML format.
        company_name (str): Name of the company.
    """
    if not sender_email or not password:
        raise ValueError("Sender email and password are required")
        
    if not recipient_email or '@' not in recipient_email:
        raise ValueError(f"Invalid recipient email: {recipient_email}")
    
    logger.info(f"Sending email to: {recipient_email}")
    try:
        # Create the email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # Create plain text version by stripping HTML
        plain_text = html_content.replace('<br>', '\n').replace('<strong>', '').replace('</strong>', '')
        
        # Attach both plain text and HTML versions
        part1 = MIMEText(plain_text, 'plain', 'utf-8')
        part2 = MIMEText(html_content, 'html', 'utf-8')
        
        msg.attach(part1)
        msg.attach(part2)

        # Attach resume
        with open(resume_path, 'rb') as file:
            resume_attachment = MIMEApplication(file.read(), Name=resume_filename)
        resume_attachment['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
        msg.attach(resume_attachment)

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            logger.info(f"Email sent successfully to {recipient_email}")

            # Log successfully sent email address to a text file
            success_log_file = f"{company_name}_successfully_sent_emails.txt"
            with open(success_log_file, 'a') as file:
                file.write(recipient_email + '\n')
            
    except Exception as e:
        logger.error(f"Failed to send email to {recipient_email}: {str(e)}")
        raise
