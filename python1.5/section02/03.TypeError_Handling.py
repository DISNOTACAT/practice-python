# x = "Seoul"
# y = 25
# z = x + y
#
# print(f'x + y : {z}')

# TypeError 발생 -> str can only concatenate to str

# 수정
x = "Seoul"
y = "25"
z = x + y

print(f'x + y : {z}') # Seoul25

# ----------------------
x = 'Seoul'
y = 25
z = x + str(y)
print(z)
# ----------------------

etc = "Korea"
print(etc())
# TypeError : is not callable

