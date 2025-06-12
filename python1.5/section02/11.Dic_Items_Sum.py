d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}
# 출력결과 : 2327

print(d.values()) # 값만 가지고 옴

# 방법1
total = 0
for i in d.values():
  total += i
print(f'결과: {total}')

# 방법2
print(f'sum 결과: {sum(d.values())}')

# 방법3
print(sum([d[item] for item in d]))

# Dict : Key와 value 구조의 자료형 (가변적-수정가능)
# get(), values(), keys()
# 빈 딕셔너리 -> d = {}
# 딕셔너리 선언 -> d = {1: 'banana', 2: 'apple'}
# 다양한 키 조합 -> d = {'name' : 'Lee', 1: [5,6,7]}
# 직접 선언 -> d = dict{[1: 'banana', 2: 'apple']}
# 시퀀스형 페어로 선언 -> d = dict([(1, 'banana'), (2, 'apple')])