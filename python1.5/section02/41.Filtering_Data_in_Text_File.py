# 텍스트 파일을 불러온 후 알파벳 C로 시작하는 나라의 지표 합을 출력

# 방법1
def read_text_file1(file_path):
  value_list = []

  with open(file_path, 'r') as f:
    # print(f.readlines())

    lines = f.readlines() # list

    for line in lines:
      country, value = line.rstrip().split(",")
      # print(country, value)

      if country.lower().startswith('c'):
        value_list.append(int (value))

  return value_list

result = read_text_file1('../source/41-1.txt')

print(sum(result))


# 방법2
import csv
# 41-2 파일 확인하기