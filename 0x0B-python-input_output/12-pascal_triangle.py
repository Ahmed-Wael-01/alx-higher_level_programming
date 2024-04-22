#!/usr/bin/python3
"""triangles everywhere"""


def pascal_triangle(n):
    """magic babe"""
    if n <= 0:
        return []
    pasc_tri = []
    for x in range(1, n + 1):
        layer = []
        for j in range(x):
            if (j == 0 or j == len(pasc_tri)):
                layer.append(1)
            else:
                layer.append(pasc_tri[x - 1][j] + pasc_tri[x - 1][j - 1])
        pasc_tri.append(layer)
    return pasc_trix
