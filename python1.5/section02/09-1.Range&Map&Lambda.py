# 1부터 15까지 원소 * 10 결과는 문자열 리스트
# range, map, lambda 사용

# range & lambda
print([str(x * 10) for x in range(1, 16)])

# map & lambda
x = map(lambda x : str(x * 10), range(1, 16))
print(list(x))