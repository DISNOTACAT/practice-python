# 예제에서 'banana' 출력하기
x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']

print(x[4])
print(x[-2])
print(x[4:5]) # ['Banana'] slicing

x.sort()
print(x[1])

x.reverse()
print(x[-2])

#-------------새롭게 알게 된 것
# index 함수
print(x.index('Banana')) # 4
print(x[x.index('Banana')])
print('Banana' in x) # True

print(x[x.index('Banana', 0, len(x))]) # 찾고자 하는 범위 지정
# print(x[x.index('Banana', 5, len(x))]) # not in list

#------------- list 함수
print(x.count('Banana'))

print(x) # 위에서 sort + reverse 상태
y = sorted(x)
print(f'x == y : {x==y}') # False
print(f'x value : {x}')
print(f'y value : {y}')

z = x + y
print(z)
print('------------------------------extend')
z2 = x.extend(y)
print(z2) # none --> extend 는 반환값 없음
print(x)

