# 사용자 비밀번호 입력
# 조건1 : 비밀번호는 반드시 8자 이상이어야 합니다.
# 조건2 : 반드시 1개 이상의 대문자는 포함되어 있어야 합니다.
# 조건3 : 반드시 1개 이상의 숫자를 포함해야 합니다.

# any 함수 : 한 개라도 참
# all 함수 : 전체가 참

# 방법 1
while True:
  results = []
  pws = input("Enter password: ")

  print()

  if not any(i.isdigit() for i in pws):
    results.append("최소 1개 이상의 숫자가 포함되어야 합니다.")

  if not any(i.isupper() for i in pws):
    results.append("최소 1개 이상의 대문자가 포함되어야 합니다.")

  if len(pws) < 8:
    results.append("패스워드 길이는 8자 이상 입력해주세요.")

  if len(results) == 0:
    print("비밀번호가 성공적으로 입력되었습니다.")
    break
  else:
    print("아래와 같이 비밀번호 조건이 맞지 않습니다.")
    for txt in results:
      print("-->", txt)