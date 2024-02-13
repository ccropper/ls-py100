"""
Write a program named age.py that asks the user to enter their age, 
then calculates and reports the future age 10, 20, 30, and 40 years 
from now. 
"""

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')


age = int(input('How old are you? '))

for year in range(10,50,10):
	print(f'In {year} years, you will be {age + year} years old.')