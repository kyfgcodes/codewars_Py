'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.'''


def duplicate_encode(word):
    word = word.lower()
    decrypted_code = ''
    for i in word:
        if word.count(i) > 1:
            decrypted_code += ')'
        else: 
            decrypted_code += '('
    return decrypted_code

print(duplicate_encode('Success'))

#Done!!!