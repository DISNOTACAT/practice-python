
origin_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def split_list(split_size=3):
  result = list()

  for i in range(0, len(origin_list), split_size):
    result.append(origin_list[i:i+split_size])

  return result

print(split_list())