# 매개변수의 기본값을 사용하기
# 1. 기본값이 모두 없어야 한다.
# 2. 기본값이 모두 있어야 한다.
# 3. 기본값이 뒤에만 있어야 한다.

# def greet (msg="Good morning!", name):
#   return "Hi! " + name + ', ' + msg

def greet (msg="Good morning!", name = "Kim"):
  return "Hi! " + name + ', ' + msg

print(greet("How do you do?", "Park"))
print(greet("How do you do?"))

def add1(a, b=10, c=15):
  print(a, b, c)
  return a+b+c
print(add1(1,2))
print(add1(b=100, c=25, a=30))

def add2(*d):
  tot = 0
  for i in d:
    tot += i
  return tot

print(add2(10)) # 10
print(add2(10, 20)) # 30

