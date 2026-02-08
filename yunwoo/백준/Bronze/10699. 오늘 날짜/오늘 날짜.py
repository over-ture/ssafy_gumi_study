from datetime import datetime, timedelta

print((datetime.utcnow() + timedelta(hours=9)).strftime("%Y-%m-%d"))
