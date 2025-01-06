import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import logging
from datetime import datetime
from scheduler.schedule_now import send_emails_now
from scheduler.send_later import schedule_emails
import email_utils.follow_up as follow_up

class EmailSenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender Application")
        self.root.geometry("600x400")
        
        # Variables
        self.xlsx_path = tk.StringVar()
        self.email_type = tk.StringVar(value="first")
        self.schedule_type = tk.StringVar(value="now")
        self.schedule_time = tk.StringVar()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Excel file selection
        ttk.Label(main_frame, text="Excel File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.xlsx_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_file).grid(row=0, column=2)
        
        # Email type selection
        ttk.Label(main_frame, text="Email Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text="First Email", variable=self.email_type, 
                       value="first").grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Follow-up Email", variable=self.email_type, 
                       value="follow-up").grid(row=1, column=2)
        
        # Schedule type selection
        ttk.Label(main_frame, text="Schedule:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text="Send Now", variable=self.schedule_type, 
                       value="now").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Schedule Later", variable=self.schedule_type, 
                       value="later", command=self.show_schedule_options).grid(row=2, column=2)
        
        # Schedule time (hidden by default)
        self.schedule_frame = ttk.Frame(main_frame)
        self.schedule_frame.grid(row=3, column=0, columnspan=3, pady=5)
        ttk.Label(self.schedule_frame, text="Schedule Time (YYYY-MM-DD HH:MM):").grid(row=0, column=0)
        ttk.Entry(self.schedule_frame, textvariable=self.schedule_time, width=20).grid(row=0, column=1)
        self.schedule_frame.grid_remove()
        
        # Send button
        ttk.Button(main_frame, text="Send Emails", command=self.send_emails).grid(row=4, column=0, 
                                                                                 columnspan=3, pady=20)
        
        # Status area
        self.status_text = tk.Text(main_frame, height=10, width=60)
        self.status_text.grid(row=5, column=0, columnspan=3, pady=5)
        
        # Configure logging to write to status area
        self.setup_logging()

    def setup_logging(self):
        class TextHandler(logging.Handler):
            def __init__(self, text_widget):
                super().__init__()
                self.text_widget = text_widget
                
            def emit(self, record):
                msg = self.format(record) + "\n"
                self.text_widget.insert(tk.END, msg)
                self.text_widget.see(tk.END)
        
        logger = logging.getLogger()
        text_handler = TextHandler(self.status_text)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        text_handler.setFormatter(formatter)
        logger.addHandler(text_handler)

    def browse_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if filename:
            self.xlsx_path.set(filename)

    def show_schedule_options(self):
        if self.schedule_type.get() == "later":
            self.schedule_frame.grid()
        else:
            self.schedule_frame.grid_remove()

    def send_emails(self):
        try:
            if not self.xlsx_path.get():
                messagebox.showerror("Error", "Please select an Excel file")
                return
                
            if self.email_type.get() == "first":
                if self.schedule_type.get() == "now":
                    send_emails_now()
                    messagebox.showinfo("Success", "Emails sent successfully!")
                else:
                    scheduled_time = self.schedule_time.get()
                    if not scheduled_time:
                        messagebox.showerror("Error", "Please enter schedule time")
                        return
                        
                    try:
                        # Validate the time format
                        datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M")
                        if schedule_emails(scheduled_time):
                            messagebox.showinfo("Success", f"Emails scheduled for {scheduled_time}")
                    except ValueError as ve:
                        messagebox.showerror("Error", "Please use format: YYYY-MM-DD HH:MM (e.g. 2024-01-05 14:30)")
                        return
            else:
                follow_up.send_follow_up_email()
                messagebox.showinfo("Success", "Follow-up emails sent successfully!")
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"Error in send_emails: {str(e)}")

def main():
    root = tk.Tk()
    app = EmailSenderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
