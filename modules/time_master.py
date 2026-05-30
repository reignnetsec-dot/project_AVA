from datetime import datetime


# Get current date and time
now = datetime.now()
# format as "YYYY/MM/DD HH:MM"
formatted_date = now.strftime("%Y/%m/%d")
formatted_time = now.strftime("%H:%M")
