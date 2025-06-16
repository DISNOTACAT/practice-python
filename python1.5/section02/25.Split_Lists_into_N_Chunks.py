
origin_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 방법1
def split_n_list1(split_size = 3):
  split_list = list()

  for i in range(0, len(origin_list), split_size):
    # print(i, i + split_size) # 인덱스 체크
    split_list.append(origin_list[i:i+split_size])

  return split_list

print('ex1: ', split_n_list1())


# 방법2
split_size = 3
output = [origin_list[i:i+split_size] for i in range(0, len(origin_list), split_size)]
print('ex2: ', output)