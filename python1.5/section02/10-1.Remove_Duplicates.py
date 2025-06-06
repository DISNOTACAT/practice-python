# 중복 되는 원소를 제거 후 출력
# Set
# List, Tuple : 순서 있음/중복 허용
# OrderedDict : Dict 순서 보장 받을 수 있음 (py3.6 부터 기본값)

x = ["a", 1 , "b", 2, "a", 3, "b", 4, 5, "b"]

ex1 = set(x)
print(list(ex1))
print()

from collections import OrderedDict
ex2 = OrderedDict.fromkeys(x)
print(list(ex2))
print()

ex3 = []
for i in x:
  if i not in ex3:
    ex3.append(i)
print(ex3)