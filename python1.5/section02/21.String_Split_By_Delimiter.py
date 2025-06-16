# 문장을 공백으로 구분 후 단어 개수를 출력
in_str = "Suppose we have few words that are seperated by spaces."
spcace_str = in_str.split()
print(len(spcace_str))

# string.split(seperator, maxsplit) : 구분자, 분할 수
# 기본 분리 지정자는 공백
# 리스트 반환

txt2 = input()
b = txt2.split("&", 1)
print(b)
