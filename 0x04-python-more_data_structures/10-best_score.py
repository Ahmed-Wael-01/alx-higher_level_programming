#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxV = None
    maxK = None
    for x in a_dictionary:
        if maxV is None or a_dictionary[x] > maxV:
            maxV = a_dictionary[x]
            maxK = x
    return maxK
