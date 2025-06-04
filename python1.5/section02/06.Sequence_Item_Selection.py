# 출력 결과 : [APPLE, KIWI]

x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]

# 방법1 - 새로운 리스트 만들기
ex1 = []
for i in range(len(x)):
  if x[i] == 'apple' or x[i] == 'kiwi':
    ex1.append(x[i].upper())
print(f'ex1 : {ex1}')
print()

#방법2 - map 함수
ex2 = filter(lambda a: a == 'apple' or a == 'kiwi', x)
print(list(ex2)) #filter object 를 형변환 시킴
print()

# filter 된 객체를 upper 시킴
ex3 = map(lambda b : b.upper(), filter(lambda a: a == 'apple' or a == 'kiwi', x))
print(list(ex3))
print()

#방법3 generator
ex4 = [a.upper() for a in x if a == 'apple' or a == 'kiwi']
print(ex4)
