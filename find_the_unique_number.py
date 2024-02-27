'''There is an array with some numbers. All numbers are equal except for one. Try to find it!'''

# def find_uniq(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i

def find_uniq(arr):
    unique = [x for x in arr if arr.count(x) == 1]
    return unique[0]

print(find_uniq([0, 1, 1]))

#Too slow??