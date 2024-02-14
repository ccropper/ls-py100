# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

nest_1_index = 0

result = []

while nest_1_index < len(my_list):
    nest_2_index = 0
    while nest_2_index < len(my_list[nest_1_index]):
        num = my_list[nest_1_index][nest_2_index]
        print(num)
        if num % 2 == 0:
            result.append(num)
        nest_2_index += 1
    nest_1_index += 1

print(result)
