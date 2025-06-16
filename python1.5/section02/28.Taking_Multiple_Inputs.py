# 사용자로부터 여러개를 입력 받고 평균값 출력하기

# 방법1
# x = int(input("Enter first value: "))
# y = int(input("Enter second value: "))
# z = int(input("Enter third value: "))
#
# print((x + y + z) / 3)

# 방법2
# x, y, z = input("Enter three values with space : ").split()
#
# print((int(x) + int(y) + int(z))/3)


# # 방법3
l = list(map(int, input("Enter three values : ").split()))
print(round(sum(l)/len(l),3))