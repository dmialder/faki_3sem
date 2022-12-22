import random


def my_decorator(random_func):
    def the_wrapper_function(list):
        num = random_func(list)
        if num > 10:
            return ("Очень много")
        elif num == 0:
            return ("Нет")
        else:
            return 0
        return num
    return the_wrapper_function

@my_decorator
def count_even_number(list):
    even_count = 0
    i = 0
    while(i < len(list)):
        if list[i] % 2 == 0:
            even_count +=1
        i += 1
    return even_count

n = random.randint(0, 15)
a = []
for i in range (n):
    a.append(random.randint(-100, 100))

print (count_even_number(a))