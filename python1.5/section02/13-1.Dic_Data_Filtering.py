#Value 값이 25 이상 필터링 후 출력하세요. 다양한 방법 으로 코딩하세요.
#출력 결과 : {'b': 33, 'd': 26, 'f': 120}

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

# 방법1
ex1 = []
for v in d.values():
  if v >= 25:
    ex1.append(v)
print(ex1)
print()

#방법2
ex2 = []
for k, v in d.items():
  if v >= 25:
    ex2.append(v)
print(ex2)
print()
print(list(dict((k,v) for k, v in d.items() if v >=25).values()))

# 방법3 Dictionary Comprehension
ex3 = dict(filter(lambda x : x[1] >= 25 , d.items()))
print(list(ex3.values()))
