# Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

print(True if student.get('name') else False)
print(True if student.get('grade') else False)

# Official solution:

print('name' in student)      # False
print('grade' in student)     # True

