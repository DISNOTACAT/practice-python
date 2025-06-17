#방법1

import os

txt_list1 = []
png_list1 = []

a = os.walk('../source/43-1') # 하위 폴더까지 순회

for root, dirnames, filenames in os.walk('../source/43-1'): # 권장 활용 방식

  # print(root, '>>>', dirnames, '>>>', filenames)
  for f in filenames:
    ext = f.split(".")[-1]

    if ext == 'txt':
      txt_list1.append(f)

    if ext == 'png':
      png_list1.append(f)

print('TXT file info : ', txt_list1, " Count : ", len(txt_list1))
print('TXT file info : ', png_list1, " Count : ", len(png_list1))

print()

# 방법2
import glob

txt_list2 = glob.glob("../source/43-1/**/*.txt", recursive=True)
png_list2 = glob.glob("../source/43-1/**/*.png", recursive=True)

print('TXT file info : ', txt_list2, " Count : ", len(txt_list2))
print('TXT file info : ', png_list2, " Count : ", len(png_list2))