# 파일을 불러와서 여러 구분자를 활용하기
# in_str = "../source/22-1.txt"

def cnt_word1(filepath):
  with open(filepath, 'r') as file:
    txt = file.read()
  txt = txt.replace(",", " ")

  #쉼표제거 확인
  # print(txt)

  txt_list = txt.split()
  # print(txt_list)

  return len(txt_list)

# print(f'ex1 결과: {cnt_word1("../source/22-1.txt")}') # 현위치 한단계 상위에서 source>>

# 방법2 정규표현식
import re

def cnt_word2(filepath):
  with open(filepath, 'r') as file:
    txt = file.read()

  # 정규표현식
  txt_list = re.split(" |,", txt) # 파이프를 기준으로, 공백과 ,로 구분하겠다.
  # print(txt_list)

  return len(txt_list)

print(f'ex1 결과: {cnt_word2("../source/22-1.txt")}')
