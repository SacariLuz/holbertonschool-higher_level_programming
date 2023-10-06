#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    name = ''

    if not a_dictionary:
        return None

    for k in a_dictionary.keys():
        v = a_dictionary[k]
        if v > max:
            max = v
            name = k
    return name
