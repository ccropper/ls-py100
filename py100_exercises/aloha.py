# Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'
count = 3

while count > 0:
    print(greeting)
    count -=1

# alternate solution using for loop and range per LS solution

for _ in range(3):
    print(greeting)