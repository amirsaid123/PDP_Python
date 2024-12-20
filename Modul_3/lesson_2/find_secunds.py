from datetime import datetime, date, timedelta, time
now = datetime.now()
first_time = datetime.fromtimestamp(0)
diff = now - first_time
print(diff.total_seconds())