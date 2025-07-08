# utils/time.py
import datetime
import re

def timestamped_filename(base: str, extension: str = "html") -> str:
    safe_base = re.sub(r"[^a-zA-Z0-9_-]", "_", base.strip().lower())
    time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    return f"{safe_base}_{time_str}.{extension}"