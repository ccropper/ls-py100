# Write code that capitalizes the words in the string 
# 'launch school tech & talk', so that you get the string 
# 'Launch School Tech & Talk'.

original_str = 'launch school tech & talk'
original_list = original_str.split(' ')
capitalized_list = [word.capitalize() for word in original_list]
capitalized_str = ' '.join(capitalized_list)
print(capitalized_str)

# using a function

def capitalize_words(string):
    if string:
        words_list = string.split(' ')
        words_capitalized = [word.capitalize() for word in words_list]
        string_capitalized = ' '.join(words_capitalized)
        return string_capitalized
    else:
        print('You provided an empty string.')
        return None

print(capitalize_words(original_str))