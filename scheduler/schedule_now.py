# scheduler/schedule_now.py

import logging
import time
from data_utils.generate_email_address import generate_email_address
from email_utils.email_sender import send_email
from email_utils.email_manager import load_email_settings, read_email_template, read_excel_data

logger = logging.getLogger(__name__)
MAX_RETRIES = 3


def send_emails_now(batch_size=10):
    """Sends emails immediately."""
    try:
        sender_email, sender_password = load_email_settings()
        email_template = read_email_template()
        data = read_excel_data()

        if not data:
            logger.error("No valid data found in Excel file")
            return

        # Process each row
        for row in data:
            try:
                first_name, last_name, email, company_name = row  # Updated tuple unpacking
                
                # Skip invalid emails
                if not email or '@' not in email or email.lower() == 'email':
                    logger.warning(f"Skipping invalid email address: {email}")
                    continue

                subject = f"Software Developer Position at {company_name}"
                message = email_template.format(
                    first_name=first_name,
                    last_name=last_name,
                    company_name=company_name
                )

                send_email(sender_email, sender_password, email, subject, message, company_name)
                logger.info(f"Email sent successfully to {email} at {company_name}")
                
            except Exception as e:
                logger.error(f"Error processing row {row}: {str(e)}")
                continue

    except Exception as e:
        logger.error(f"Error in send_emails_now: {str(e)}")
        raise
