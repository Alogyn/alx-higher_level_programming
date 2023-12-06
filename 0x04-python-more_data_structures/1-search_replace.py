#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [element if element != search
                else replace for element in my_list]

    return (new_list)
