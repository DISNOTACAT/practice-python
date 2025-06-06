#json 형식을 예쁘게 출력하기
from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

response_json = response.read()

d = json.loads(response_json)

# 출력 결과 비교(print)
print(d)

# 출력 결과 비교(pprint)
from pprint import pprint

pprint(d)
