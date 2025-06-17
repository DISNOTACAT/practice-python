# Dict 선언
d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

# # 사용자 입력1(정상 값) : France
# # 출력1 : '32'
# # 사용자 입력2(잘못된 값) : Canada
# # 출력2 : 'No results were found for your search.'

# 연습
# str = input()
# if d.__contains__(str):
#   print(d[str])
# else:
#   print('No results were found for your search.')

# 방법1
# def search_dict(word):
#   try:
#     c = dict((new_k.lower(), new_val) for new_k, new_val in d.items())
#     return c[word]
#   except:
#     return 'No results were found for your search.'
#
# txt = input("Enter key: ").lower()
# print(search_dict(txt))


# 방법2
def search_dict2(word):
  c = dict((new_k.lower(), new_val) for new_k, new_val in d.items())
  return c.get(word, 'No results were found for your search.') # 있으면, 없으면


txt = input("Enter key: ").lower()
print(search_dict2(txt))
