# FirstReach - Cold Email Automation for Job Seekers (Personalized)

## Overview

This project automates the process of sending cold emails from a job seeker (you) to recruiters. It utilizes common email address patterns to generate potential email addresses for recruiters based on their first name, last name, and company name. The goal is to save you time and effort by streamlining the process of reaching out to recruiters for potential job opportunities.

## How It Helped Me Save Time

As a job seeker, I used to spend over 3 hours every day sending cold emails to recruiters in various companies. However, this manual process was time-consuming and often led to fatigue and burnout. With the implementation of this cold email automation project:

- **Time Savings**: By automating the email sending process, I was able to significantly reduce the time spent on reaching out to recruiters. What used to take me hours to accomplish manually can now be done within minutes using this automated solution. For instance - once I had names of folks from a company, i was able to send over 50 emails in a few minutes.

    ![Gmail Screenshot](./output_img/output_img.png.png)

- **Efficiency**: The project generates potential email addresses for recruiters based on common patterns, such as firstname@company.com, firstname.lastname@company.com, and firstnamelastname@company.com. This streamlined approach allows me to quickly send personalized cold emails to a large number of recruiters in less time.

- **Increased Productivity**: With the time saved from manual email sending, I can now allocate more time to other aspects of my job search, such as networking, skill development, and preparing for interviews. This increased productivity has helped me make significant progress in my job search journey.


## Features

- **Email Address Generation**: The project automatically generates potential email addresses for recruiters based on common patterns, saving you the hassle of manually guessing email addresses.

- **Personalized Cold Emails**: You can send personalized cold emails to recruiters using a predefined email template. The emails contain relevant information, such as your name, target company, designation and a customized message.

- **Attachment Support**: The project supports attaching files, such as resumes, to the cold emails, allowing you to provide additional information to recruiters.

- **Bulk Email Sending:** The project supports sending bulk emails to multiple recruiters simultaneously, allowing you to reach out to a large number of potential employers with minimal effort.

- **Scheduled Email Delivery**: Schedule email delivery for a specific time, allowing you to reach recipients at the most convenient time for them.

- **Batch Processing**: Emails are sent in batches, allowing for smoother processing and reducing the risk of errors or timeouts when sending a large number of emails.

- **Retry Logic**: In case of any errors encountered during email sending, the project includes a retry mechanism. It will attempt to resend the email for a maximum of 3 times before logging an error message if it fails.

- **Follow-Up Emails**: Send follow-up emails to recruiters who have not responded to your initial email, increasing your chances of getting a response.


## Usage

### Step 1: Prepare Data

1. **Open Excel Spreadsheet**: Open an Excel spreadsheet (e.g., Microsoft Excel, Google Sheets) on your computer.

2. **LinkedIn Search**: Visit LinkedIn (www.linkedin.com) and search for the recruiters or employees by company name. Often, you can find their profiles with their first and last names listed.

3. **Record Information**: Record the first name and last name of the recruiters or employees found on LinkedIn in your Excel spreadsheet. This will ensure that you have accurate data to use in the email generation process. In the spreadsheet, create columns for "First Name," "Last Name," "Email,", "Company Name" and "Desingation" Enter the relevant information for each recruiter or employee in the respective rows. If the recruiter or employee's email address is available, enter it in the "Email" column. If not, leave the "Email" column blank.

### Step 2: Update Resume File Name

1. **Locate Your Resume**: Find your resume file on your computer. Make sure it's in PDF format and is named appropriately (e.g., "YourName_Resume.pdf").

### Step 3: Update Environment Variables

1. **Create .env File**: Create a new text file on your computer and rename it to `.env` (make sure it doesn't have a `.txt` extension).

2. **Enter Email Credentials**: Open the `.env` file with a text editor (e.g., Notepad, TextEdit) and enter your email credentials in the following format:

   ```plaintext
   EMAIL_USERNAME=your_email@gmail.com
   PASSWORD=your_email_password
   SENDER_NAME=Your Name
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

   Replace `your_email@gmail.com` with your email address and `your_email_password` with your email password.

### Step 4: Update Email Template File

1. **Choose Email Template**: Decide whether you want to use a formatted or plain text email template.

2. **Open Email Template File**: Locate the `email_template.txt` file in the project directory and open it with a text editor.

3. **Customize Email Content**: Modify the content of the email template to include a personalized message to recruiters or employees. You can include placeholders like `{first_name}`, `{last_name}`, `{company_name}`, and `{email}` to personalize each email.

   - If you want to send plain text emails, leave the formatting as is.
   - If you want to format your emails (e.g., bold, italics), uncomment the relevant lines in the template file and customize the formatting as desired.

### Step 5: Using the GUI Application

1. **Launch the Application**: Run `python main.py` to start the GUI application.

2. **Select Excel File**: 
   - Click the "Browse" button to select your Excel file containing recruiter information
   - Make sure the Excel file has columns for: First Name, Last Name, Email, Company Name, and Designation

3. **Choose Email Type**:
   - Select "First Email" for initial outreach
   - Select "Follow-up Email" for follow-up messages

4. **Select Sending Option**:
   - Choose "Send Now" to send emails immediately
   - Choose "Schedule Later" to schedule emails for a specific time

5. **Schedule Time (if applicable)**:
   - When "Schedule Later" is selected, enter the date and time in format: YYYY-MM-DD HH:MM
   - Example: 2024-01-05 14:30 (for January 5th, 2024 at 2:30 PM)

6. **Send Emails**:
   - Click "Send Emails" button to execute your selection
   - Monitor the status area at the bottom for progress and any error messages

### Important Notes:

- **Scheduling**: The application must remain running for scheduled emails to be sent
- **Time Format**: Always use 24-hour format when scheduling (e.g., 14:30 instead of 2:30 PM)
- **Status Updates**: Check the status area for real-time feedback and error messages
- **Excel Format**: Ensure your Excel file matches the required format with all necessary columns

### Screenshots

#### Immediate Email Sending
![Email Now](./output_img/email_sent_now.png.png)

#### Scheduled Email Sending
![Email Later](./output_img/email_sent_later.png.png)

## Dependencies

- Python 3.x
- tkinter (for GUI)
- openpyxl (Excel file handling)
- python-dotenv (environment variables)
- logging (status tracking)
