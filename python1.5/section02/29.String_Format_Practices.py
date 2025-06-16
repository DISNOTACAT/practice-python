# String Format Practices

# 공통 변수 선언
x = 10
y = 20
serialno = 2087457
n = 'Kim'


# 출력1
ex1 = 'n = %s, s = %d, sum=%d' % (n, serialno, (x+y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=serialno, sum=x+y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {serialno}, sum={x+y}'
print(ex3)

# 출력4
from string import Template
ex4 = 'n = $n, s = $serialno, sum = $sum'

t = Template(ex4)
t.substitute(n=n, serialno=serialno, sum=(x+y))

# 출력5 (다양한 f-string연습)

# 진수
# (2진수: b, 8진수 : o, 16진수: x|X)
k = 77

print(f"k 2: {k:b}, k 8: {k:o}")
print(f"k 16: {k:x}, k 16: {k:X}")


# 구분기호
m = 1000000000
print(f'm: {m:,}')
print()


# 정렬
# ^ : 가운데, < :왼쪽, > :오른쪽

g = 20
print(f'g space :{g:10}.')
print(f'g center:{g:^10}.')
print(f'g left  :{g:<10}.')
print(f'g right :{g:>10}.')

# 채우기
print(f'g center:{g:-^10}.') # g center:----20----.
print(f'g left  :{g:*<10}.') # g left  :20********.
print(f'g right :{g:$>10}.') # g right :$$$$$$$$20.







# 파이썬 문자 출력 방법
# 1. % Operator (Old Style)
# 2. str.format (New Style)
# 3. f-String (Pyhon 3.6+)
# 4. Template String(from string import Template)

