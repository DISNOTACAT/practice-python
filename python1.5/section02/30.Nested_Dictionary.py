# 중첩 Dict 선언
d = {"group1":[
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


# 출력결과
# Name : Kim, Age : 23, Type : officer
# kets() get() items()

# 방법1
ex1 = 'Name : {0}, Age : {1}, Type : {2}'.format(d['group2'][0]['name'], d['group2'][0]['age'], d['type']['b'])
print(ex1)
print()

# 방법2
ex2 = 'Name : {0}, Age : {1}, Type : {2}'.format(d.get('group2')[0].get('name'), d.get('group2')[0].get('age'), d.get('type')['b'])
print(ex2)