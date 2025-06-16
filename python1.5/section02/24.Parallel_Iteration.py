# 리스트를 dict 구조로 변경하기

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# 방법1
result1 = {}

for x, y, z in zip(a, b, c):
  result1[x] = y * z

print('ex1 결과: ', result1)

# 방법2
print('ex2: ', {x: y * z for x, y, z in zip(a, b, c)})

# 방법3
print('ex3: ', dict((x, y * z) for x, y, z in zip(a, b, c)))