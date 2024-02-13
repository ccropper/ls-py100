# Write a function that takes a string as an argument and returns 
# an all-caps version of the string when the string is longer than 
# 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 
# 'goodbye'.

def conditionally_cap_string(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str

str = input('Give me a string: ')
print(f'Here\'s your string back: {conditionally_cap_string(str)}')

