# Write a function that computes and returns the factorial of a number by 
# using a for or while loop. The factorial of a positive integer n, signified 
# by n!, is defined as the product of all integers between 1 and n, inclusive:

def find_factorial_using_while(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

def find_factorial_using_for(number):
    result = 1
    for n in range(number, 0, -1):
        # print(f'n is now: {n}')
        result *= n
        # print(f'result is now {result}')
    return result

num = int(input('Give me a number: '))
factorial = find_factorial_using_while(num)

print(f'The factorial of {num} is {factorial}')

num = int(input('Give me another number: '))
factorial = find_factorial_using_for(num)

print(f'The factorial of {num} is {factorial}')
