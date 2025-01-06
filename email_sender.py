from datetime import datetime
import time

# ...existing code...

def schedule_emails(scheduled_time):
    try:
        # Parse the scheduled time
        scheduled_datetime = datetime.strptime(scheduled_time, "%H:%M").time()
        current_time = datetime.now().time()
        
        # Calculate wait time in seconds
        target_time = datetime.combine(datetime.today(), scheduled_datetime)
        current_datetime = datetime.combine(datetime.today(), current_time)
        wait_seconds = (target_time - current_datetime).total_seconds()
        
        if wait_seconds < 0:
            # If time has passed, schedule for next day
            wait_seconds += 24 * 3600
            
        # Sleep until scheduled time
        time.sleep(wait_seconds)
        
        # Send emails
        send_emails_now()
        
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM format (24-hour)")
    except Exception as e:
        raise Exception(f"Failed to schedule emails: {str(e)}")

# ...existing code...
