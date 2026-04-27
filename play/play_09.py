from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo  # tzdata

dt1 = datetime.now(tz=ZoneInfo('Europe/Moscow'))
dt1 = datetime(dt1.year, dt1.month - 3, dt1.day, dt1.hour, dt1.minute, dt1.second, dt1.microsecond, tzinfo=ZoneInfo('Europe/Moscow'))
dt2 = datetime.now(tz=ZoneInfo('Asia/Shanghai'))
print(dt1, type(dt1))
print(dt2, type(dt2))
time_delta = dt2 - dt1
print(time_delta)
print(time_delta.seconds // 60)
print(dt1.strftime('%B'))
dt3 = dt1 - timedelta(days=45)
print(dt3.strftime('%B'))
