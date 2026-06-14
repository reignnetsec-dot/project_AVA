from datetime import datetime


def get_current_datetime():
    now = datetime.now()
    return {
        "date": now.strftime("%Y/%m/%d"),
        "time": now.strftime("%H:%M")
    }
