import math
import random
# recursive implementation of binary search in Python

def binary_search(enemy_list, enemy_numb):
    """Performs recursive binary search of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    lower_bound = 0
    upper_bound = len(enemy_list) - 1

    if len(enemy_list) == 0:
        return '{item} was not found in the list'.format(item=item)
    else:
        current = (lower_bound + upper_bound) // 2
        if enemy_numb == enemy_list[current]:
            return '{enemy_numb} found'.format(enemy_numb=enemy_numb)
        else:
            if enemy_list[current] < enemy_numb:
                return binary_search(enemy_list[current+1:], enemy_numb)
            else:
                return binary_search(enemy_list[:current], enemy_numb)

enemy_list = ["enemy_1.png","enemy_2.png","enemy_3.png","enemy_4.png","enemy_5.png","enemy_6.png","enemy_7.png","enemy_8.png","enemy_9.png"]
enemy_numb = math.ceil(random.randrange(1,9))
enemy_numb = str(enemy_numb)
enemy_numb = "enemy_" + enemy_numb + ".png"

enemy_pic = binary_search(enemy_list,enemy_numb)
print(enemy_pic)
