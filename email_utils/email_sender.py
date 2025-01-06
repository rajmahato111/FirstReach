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

def send_email(sender_email, sender_password, recipient_email, subject, message, company_name):
    """
    Sends an email with an attachment.
    
    Args:
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Email subject.
        message (str): Email body message.
        company_name (str): Name of the company.
    """
    if not sender_email or not sender_password:
        raise ValueError("Sender email and password are required")
        
    if not recipient_email or '@' not in recipient_email:
        raise ValueError(f"Invalid recipient email: {recipient_email}")
    
    logger.info(f"Sending email to: {recipient_email}")
    try:
        server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
        server.starttls()
        
        try:
            server.login(sender_email, sender_password)
        except (smtplib.SMTPAuthenticationError, AttributeError) as e:
            logger.error(f"Authentication failed for {sender_email}")
            logger.error("Please check your Gmail settings and .env file")
            raise
            
        msg = MIMEMultipart()
        # Use formataddr to set sender's name and email
        sender_name = os.getenv('SENDER_NAME', 'Raj Kumar')  # Get from env or use default
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        # msg.attach(MIMEText(message, 'html')) - uncomment if you want your message to be formatted
        
        with open(resume_path, 'rb') as file:
            resume_attachment = MIMEApplication(file.read(), Name=resume_filename)
        resume_attachment['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
        msg.attach(resume_attachment)
        
        server.sendmail(sender_email, recipient_email, msg.as_string())
        logger.info(f"Email sent successfully to {recipient_email}")

        # Log successfully sent email address to a text file
        success_log_file = f"{company_name}_successfully_sent_emails.txt"
        with open(success_log_file, 'a') as file:
            file.write(recipient_email + '\n')

        server.quit()
    except Exception as e:
        logger.error("Error sending email:", exc_info=True)
        raise e
