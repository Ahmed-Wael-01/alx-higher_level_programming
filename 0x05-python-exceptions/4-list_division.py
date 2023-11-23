#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    tmp = 0
    while i < list_length:
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            tmp = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except IndexError:
            print("out of range")
            tmp = 0
        finally:
            new_list[i] = tmp
            i += 1
    return new_list

