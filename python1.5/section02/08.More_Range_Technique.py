# 1부터 20까지 홀수 = num * 10, 짝수는 그대로 출력하기
a = []
for i in range(1, 21):
  if(i % 2 != 0):
    a.append(i * 10)
  else:
    a.append(i)
print(a)

# ---------------
# List Comprehension : 짧은 문법(Syntax)으로 간단하게 조건에 맞는 리스트 생성
# [조건 만족 시 출력값 if 조건 else 조건 불만족 출력 값 for i in list]
z = [x * 10 if x % 2 != 0 else x for x in range(1,21)]
print(f'List Comprehension 결과 : {z}')


# ------------------------
print([[j for j in range(5)] for i in range (5)])