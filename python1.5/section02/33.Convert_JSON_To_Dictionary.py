d = """
    {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    """

import json

# 방법1
result1 = json.loads(d.replace("'","\"")) # 따옴표 통일화 필요

# 출력
print(result1)
print()

# 방법2
with open("../source/33-1.json", "r") as out:
  result2 = json.load(out)

  print(result2)
  print(type(result2)) # <class 'dict'>
