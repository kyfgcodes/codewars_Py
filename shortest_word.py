'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

def find_short(word):
    for i in word:
        if len(i) is min(word):
            return len(i)
    
print(find_short("bitcoin take over the world maybe who knows perhaps"))
    
