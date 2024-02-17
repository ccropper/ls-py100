# Use a for loop to iterate over the numbers dictionary and return a 
# list containing each number divided by 2. Assign the returned list 
# to a variable named half_numbers and print its value using print.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

half_numbers = []
for value in numbers.values():
    half_numbers.append(value // 2)

# Expected output: [50, 25, 5]
print(half_numbers)
