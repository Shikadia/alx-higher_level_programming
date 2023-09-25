#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists, element by element.

    Parameters:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Return: A new list containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
    return new_list
