students = {}
count = int(input("Enter no. of students: "))
for i in range(count):
    name = input("Enter Name: ")
    roll_no = int(input("Enter Roll no. "))
    students[roll_no] = name
print(students)
'''
for name in students.values():
    print(name)

for roll in students.keys():
    print(roll, students[roll])

for stud_name, rollNo in students.items():
    print(stud_name,rollNo)
'''
