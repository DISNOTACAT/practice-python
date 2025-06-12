d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}
# 출력결과 : 2327


# 방법1
print(sum(d.values()))
print()

# 방법2
total = 0
for i in d.values():
  total += i
print(total)
print()

# 방법3
print(sum(d[i] for i in d))