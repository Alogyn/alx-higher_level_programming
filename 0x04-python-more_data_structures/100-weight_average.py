#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    total_score = 0
    total_weight = 0

    for tuppl in my_list:
        total_score += (tuppl[0] * tuppl[1])
        total_weight += tuppl[1]

    average = total_score / total_weight

    return (average)
