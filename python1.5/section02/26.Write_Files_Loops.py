import os

# 파일명 & 경로 = "../source/26-1/파일명.txt"
filenames = ["A", "B", "C", "D", "F", "G"]
contents1 = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
contents2 = [["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"], ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"], ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"], ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"], ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"], ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]]

#방법1
def write_contents1(filepath):

  # 지정경로의 폴더를 만들어줌 (os에 권한을 줌)
  if not os.path.exists(filepath):
    os.mkdir(filepath)

  # loop write
  for n, c in zip(filenames, contents1):
    with open(filepath + n + '.txt', 'w') as file:
      file.write(c) # 리스트 요소 하나씩 파일로 저장

# 실행1
write_contents1("../source/26-1/")


#방법2 - writelines
def write_contents2(filepath):

  # 지정경로의 폴더를 만들어줌 (os에 권한을 줌)
  if not os.path.exists(filepath):
    os.mkdir(filepath)

  # loop write
  for n, c in zip(filenames, contents2):
    with open(filepath + n + '.txt', 'w') as file:
      file.writelines(c + "\n" for c in c) # 리스트 안의 리스트를 다룸
# 실행2
# write_contents2("../source/26-1/")