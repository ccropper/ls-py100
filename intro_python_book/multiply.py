"""
Write a program that uses a multiply function to multiply two 
numbers and returns the result. Ask the user to enter the two 
numbers, then output the numbers and result as a simple equation.
"""

def multiply(first_number, second_number):
	return float(first_number) * float(second_number)

first_number = input("Enter a number: ")
second_number = input("Enter another number: ")
product = multiply(first_number, second_number)

print(f'{first_number} x {second_number} = {product}')