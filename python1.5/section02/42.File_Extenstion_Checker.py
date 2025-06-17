# 폴더 42-1 에 존재하는 파일 중에서 확장자 가 *.py 및 *.png 파일을 분류하세요.
# ../source/42-1
# 조건1 : 파이썬 실행 형식(*.py) 개수 및 파일명
# 조건2 : 이미지 파일 형식(*.png) 개수 및 파일

# 방법1
import os
# files = os.listdir('../source/42-1')
# print(files)

png_list1 = []
py_list1 = []

for f in os.listdir('../source/42-1'):
  # print(os.path.splitext(f)) # {'파일명','확장자'}
  # print(f.split(".")[-1]) # 확장자만 추출

  ext = f.split(".")[-1]

  if ext == 'png':
    png_list1.append(f)

  if ext == 'py':
    py_list1.append(f)


print(f'PNG : ', png_list1, " Count : ", len(png_list1))
print(f'PY : ', py_list1, " Count : ", len(py_list1))

print()

# 방법2
import glob

png_list2 = glob.glob1("../source/42-1", "*.png")
py_list2 = glob.glob1("../source/42-1", "*.py")

print(f'PNG : ', png_list2, " Count : ", len(png_list2))
print(f'PY : ', py_list2, " Count : ", len(py_list2))