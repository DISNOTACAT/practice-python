# Dict 선언
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


# 추가 # "group1" : {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}
# 추가2 # "type" : {"f": "engineer"}


# 방법1
# d['group1'].append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
# d['type'].update({"f": "engineer"})

print(d.items())
print()

# 방법2
d.get('group1').append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
d.get('type')['f'] = "engineer"
print(d.items())
