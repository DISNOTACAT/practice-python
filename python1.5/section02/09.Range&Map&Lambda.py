# 1부터 15까지 원소 * 10 결과는 문자열 리스트
# range, map, lambda 사용

# range & lambda
a = [str(i * 10) for i in range(1, 16)]
print(a)

# map
b = (map(lambda x : str(x * 10), range(1,16)))
print(list(b))
