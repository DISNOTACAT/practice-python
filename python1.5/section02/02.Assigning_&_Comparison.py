# 예제1
x = 15
y = 25

print(f'x == y : {x == y}')
print('my answer : False')
print(f'x is y : {x is y}')
print('my answer : False')
print()
# hex() : 정수를 16진수 문자열로 반환
print(f'x value, id : {x}, {hex(id(x))}')
print(f'y value, id : {y}, {hex(id(y))}')

print('------------------------')

# 예제2
x = ['orange', 'banana', 'apple']
y = x

print(f'x == y : {x == y}')
print('my answer : True')
print(f'x is y : {x is y}')
print('my answer : True')
print()
print(f'x value, id : {x}, {hex(id(x))}')
print(f'y value, id : {y}, {hex(id(y))}')

print('------------------------')

# 예제3
x = ['orange', 'banana', 'apple']
y = ['orange', 'banana', 'apple']

print(f'x == y : {x == y}')
print('my answer : True')
print(f'x is y : {x is y}')
print('my answer : False')
print()
print(f'x value, id : {x}, {hex(id(x))}')
print(f'y value, id : {y}, {hex(id(y))}')