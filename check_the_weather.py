weather = 'cloudy'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")


# rewrite as a match-case statement

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")