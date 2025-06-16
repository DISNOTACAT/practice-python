# 리스트를 dict 구조로 변경하기

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# 방법1
result = {}

for x, y, z in zip(a, b, c):
  result[x] = y*z

print(result)