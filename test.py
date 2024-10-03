import datetime
from datetime import timedelta
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d")
now_day = datetime.datetime.now() + timedelta(days=1)
now_day = now_day.strftime("%Y-%m-%d")

print(now)
print(now_day)