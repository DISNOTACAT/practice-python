# Dict 선언
d = dict(one=list(range(1, 11)), two=list(range(11, 23)),
         three=list(range(23, 37)))

# # 출력 결과
#
# key 'one' has values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> total : 10
# key 'two' has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] -> total : 12
# key 'three' has values [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] -> total : 14

print(f'key \'one\' has values {d.get("one")}')
print()

for k, v in d.items():
  print(f'key "{k}" has values {v}')
