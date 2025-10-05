import datetime


def log_message(msg):
    """Log message with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")


def to_int(value):
    """Convert safely to int."""
    try:
        return int(value)
    except Exception:
        return None
