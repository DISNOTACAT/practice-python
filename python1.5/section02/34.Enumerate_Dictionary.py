l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]
# list를 dict으로 형변환 하면서, enumerate를 활용해서 반복된 숫자를 자동으로 설정

# 출력 1
d1 = dict(enumerate(l))

print(d1) # {0: 'Red', 1: 'Green', 2: 'Black', 3: 'Blue', 4: 'Orange', 5: 'Purple'}


# 출력2
d2 = dict(enumerate(l, start=100)) # {100: 'Red', 101: 'Green', 102: 'Black', 103: 'Blue', 104: 'Orange', 105: 'Purple'}
print(d2)