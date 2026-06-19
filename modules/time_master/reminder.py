import schedule
import time
import datetime
import json
import os


DEFAULT_DATA = {
    "last_study_session": None,
    "study_streak": 0,
    "total_study_count": 0,
    "study_log": [],
    "settings": {
        "reminder_times": ["09:00", "14:00", "19:00"],
        "email_enabled": True,
        "system_notification_enabled": True,
        "email_recipient": "your_email@gmail.com"
        }
    }


class StudyTracker:
    """Manages study data persistance"""
    


    def __init__(self, json_file_path):
        self.json_file = json_file_path



    def load_data(self):
        """Read JSON file"""
        # Handle: file exists vs file doesn't exist
        if not os.path.exists(self.json_file):
            self.save_data(DEFAULT_DATA.copy())
            return DEFAULT_DATA.copy()
        
        try:
            with open(self.json_file, "r", encoding="utf-8") as handle:
                return json.load(handle)
        except (json.JSONDecodeError, OSError):
            self.save_data(DEFAULT_DATA.copy())
            return DEFAULT_DATA.copy()


    def save_data(self, data):
        """Write to JSON file"""
        with open(self.json_file, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)


    def update_streak(self):
        """Update streak if studied today"""


    def add_study_session(self, subject, duration):
        """Log a new study session"""
        now = datetime.datetime.now().isoformat(timespec="seconds")
        session = {
            "timestamp": now,
            "subject": subject,
            "duration_minutes": duration
        }


class NotificationManager:
    """Handles both system and email notifications"""


    def __init__(self, email_config=None):
        self.email_config = email_config


    def send_system_notification(self, title, message):
        """Use notify-send (Linux)"""

        
    def send_email(self, subject, body):
        """Use smtplib for Gmail"""

        
    def send_both(self, title, message, email_subject, email_body):
        """Send both simultaneously"""


class MessageGenerator:
    """Generates motivational messages and suggestions"""
    
    def get_motivational_message(self):
        """Random motivational quote"""
        
    def get_subject_suggestion(self):
        """Random topic to study"""
        
    def get_study_duration_suggestion(self):
        """Suggested study time"""
        
    def build_reminder_message(self, include_streak=True):
        """Composite message with all elements"""


class ReminderScheduler:
    """Orchestrates the entire reminder system"""
    
    def __init__(self, tracker, notifier, message_gen):
        self.tracker = tracker
        self.notifier = notifier
        self.message_gen = message_gen
    
    @schedule_task("09:00")
    def morning_reminder(self):
        """Morning study reminder"""
        
    @schedule_task("14:00")
    def afternoon_reminder(self):
        """Afternoon study reminder"""
    
    def run(self):
        """Main loop - keeps scheduler running"""


def log_reminder(func):
    """Decorator: logs each reminder sent"""
    def wrapper(self, *args, **kwargs):
        # Call the original function
        result = func(self, *args, **kwargs)
        # Log to JSON that reminder was sent
        return result
    return wrapper

def schedule_task(time_str):
    """Decorator: schedules a method to run at specific time"""
    def decorator(func):
        # Attach scheduling metadata to the function so it can be
        # scheduled when an instance of the class is created.
        setattr(func, "_schedule_time", time_str)
        return func
    return decorator