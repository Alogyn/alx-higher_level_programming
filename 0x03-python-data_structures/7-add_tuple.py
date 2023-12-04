#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        a1 = tuple_a[0]
    else:
        a1 = 0

    if len(tuple_a) > 1:
        a2 = tuple_a[1]
    else:
        a2 = 0

    if len(tuple_b) > 0:
        b1 = tuple_b[0]
    else:
        b1 = 0

    if len(tuple_b) > 1:
        b2 = tuple_b[1]
    else:
        b2 = 0

    sum_1 = a1 + b1
    sum_2 = a2 + b2

    return (sum_1, sum_2)
