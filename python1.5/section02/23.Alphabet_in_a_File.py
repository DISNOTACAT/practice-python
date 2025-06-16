# 알파벳 쓰기 -> 파일로 작성하기


# 방법1

def write_alphabet1(filepath):
  with open(filepath, 'w') as file:
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #Str은 시퀀스형
      file.write(letter + " ")


print(f'연습 결과: {write_alphabet1("../source/23-1.txt")}')

# 방법2 - string
import string

def write_alphabet2(filepath):
  with open(filepath,"w") as file:
    for letter in string.ascii_uppercase:
      file.write(letter + "\n")

print(f'연습 결과: {write_alphabet2("../source/23-2.txt")}')
