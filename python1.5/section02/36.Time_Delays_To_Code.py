# time.sleep(secs)
import time

# 방법1
# n = 0
# while n < 10:
#   n += 1
#   time.sleep(1) # sleep으로 인해 비동기 프로세스의 영향성을 주의해야함
#   print(n)

# 방법2
# n = 0
# while True:
#   n += 1
#   time.sleep(1)
#   print(n)
#
#   if n == 10 :
#     break

# 방법3
n = 1
while True:
  time.sleep(1)
  print(n)

  n+=1
  if n > 10:
    break
