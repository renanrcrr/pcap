#!/usr/bin/env python3
""" list_utils.py is a sample Python module that exposes list utility functions """

__usage_counter = 0

def sum_elements(user_list):
    global __usage_counter
    __usage_counter += 1
    element_sum = 0
    for el in user_list:
        element_sum += el
    return element_sum

def double_each_element(user_list):
    global __usage_counter
    __usage_counter += 1
    return [element * 2 for element in user_list]

def get_usage_counter():
    global __usage_counter
    return __usage_counter

if __name__ == '__main__':
    print('Module executed independently, running tests...')
    entry_list = [1, 2, 3, 4, 5]
    
    summed = sum_elements(entry_list)
    if summed == 15:
        print('Sum list OK')
    else:
        print('Sum list failed')
    
    doubled = double_each_element(entry_list)
    if doubled == [2, 4, 6, 8, 10]:
        print('Doubled list OK')
    else:
        print('Doubled list failed', doubled)
        
    counter = get_usage_counter()
    if counter == 2:
        print('Usage counter OK')
    else:
        print('Usage counter failed')