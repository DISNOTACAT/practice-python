# 파이썬에 제공이 되지 않는 수학 공식을 구현하자

# 방법1
def sigma_sum1(n):
  tot = 0
  for i in range(1, n+1):
    tot += i
  return tot

print(f'ex1 결과: {sigma_sum1(100)}')

# 방법2
def sigma_sum2(n):
  return n * (n + 1) // 2
print(f'ex2 결과: {sigma_sum2(100)}')

# 방법3
def sigma_sum3(n):
  return sum(range(n+1))
print(f'ex3 결과: {sigma_sum3(100)}')

