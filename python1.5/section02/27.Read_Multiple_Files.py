import os

def read_text_file1(file_path):
  outputs = []

  for file in os.listdir(file_path):
    # 파일 리스트 확인
    # print(file)

    if file.endswith(".txt"):

      target_path = f"{file_path}/{file}"

    with open(target_path, 'r') as f:

      # print(f.read())
      outputs.append(f.read().strip('\n'))

  return outputs
#실행
# print(read_text_file1("../source/27-1/"))


# 방법2
import glob

def read_text_file2(file_path):
  outputs = []

  for file in glob.glob(file_path + "/*.txt"):

    with open(file, 'r') as f:
      # print(f.read())
      outputs.append(f.read().strip('\n'))

  return outputs
#실행
print(read_text_file2("../source/27-1/"))
