import random

len_list = []
famous_len_list = []


def rand_list():
    rand_lst = []
    while True:
        a = random.randint(0, 1000)
        if a not in rand_lst:
            rand_lst.append(a)
        else:
            return len(rand_lst)


def find_average_len():
    for i in range(1000):
        len_ = rand_list()
        len_list.append(len_)
    return sum(len_list) / len(len_list)


average_len = find_average_len()
print(average_len)
