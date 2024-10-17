people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

for name in people.values():
    for key, values in name.items():
      
        if values=='27':
            print(name['name'])
