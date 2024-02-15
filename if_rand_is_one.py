# Write an if statement that prints Yes! if random_number is 1, and 
# No. if random_number is 0.

import random
random_number = random.randint(0, 1)

if random_number == 1:
    print("Yes!")
else:
    print("No.")

# ternary

print("Yes!" if random_number == 1 else "No.")