'''Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!'''


def get_sum(a):
    num_list = [0]
    for i in range(-a + 1):

        num_list.append(i + 1)
    return num_list

print(get_sum(-3))


