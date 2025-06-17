# package datetime
# strftime()

from datetime import datetime, timezone

# 타임존 출력 : 2025-06-17 01:41:08.600381+00:00
print(datetime.now(timezone.utc))

# 출력1 : 2025-06-17 10:41:08
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 출력2 : 2025-06-17 10:42:01 AM Tuesday June
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p %A %B'))

# 출력3 : Tuesday, June, 17, 2025 10:42:47
print(datetime.now().strftime('%A, %B, %d, %Y %H:%M:%S'))
print(datetime.now().strftime('%A, %B, %d, %Y %T'))

# 출력4 : Tuesday, Jun, 06/17/25 10:43:33 AM
print(datetime.now().strftime('%A, %b, %x %r'))
# 출력4 : Tuesday, Jun, 06/17/25 10:43
print(datetime.now().strftime('%A, %b, %x %R'))