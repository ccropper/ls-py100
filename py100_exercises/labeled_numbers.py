# Use a for loop to iterate over the numbers dictionary and print 
# each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

def print_dict(d):
    for key, value in d.items():
        print(f'A {key} number is {value}.')

print_dict(numbers)

