# random.choice : 1개 생성
# random.choices : n개 생성 (중복x) python3.6+
# random.sample : n개 생성 (중복o)

import random
from datetime import datetime

# 중복 제거 고려
# 1. seed 사용
# 2. set() 사용
# 3. 반복문 체크

# 방법1
def generate_coupon_code(n):
  characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

  code_list = []

  random.seed(100)
  # 'None' (default로 적지 않아도됨)
  # 인자 넣으면, 생성 값이 변경되지 않음.

  for i in range(0, n):
    chosen = random.sample(characters, 6)

    code = "".join(chosen)
    code_list.append(code)

  return code_list

print(generate_coupon_code(5))

