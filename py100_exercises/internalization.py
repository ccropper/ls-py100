# Use Python's control structures to create a function that takes an 
# ISO 639-1 language code and returns a greeting in that language. 
# You can take the examples below or add whatever languages you like.

def greet(lang_code):
    match lang_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

print('results from calling the greet function:')
print('')
print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print('')
# Building on your solutions from the previous exercises, write a 
# function local_greet that takes a locale as input, and returns 
# a greeting. 

def extract_language(locale):
    locale_split = locale.split('_')
    return locale_split[0]

def extract_region(locale):
    return locale.split('_')[1].split('.')[0]


def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    match (language, region):
        case ('en', 'US'):
            return 'Hi!'
        case ('en', 'GB'):
            return 'G\'Day!'
        case ('en', 'AU'):
            return '\'ello Mate!'
        case _:
            return greet(language)

print('results from calling the local_greet function:')
print('')
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!