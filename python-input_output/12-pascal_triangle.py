#!/usr/bin/python3

   ''' Defines function that prints pascals triangle '''


def pascal_triangle(n):

    ''' Defines a function named pascal_triangle that takes one parameter ''' 

    if n <= 0:
        return []

    ''' If n is 0 or negative, return an empty list '''

    triangles = [[1]] 

    ''' Start the triangle with the first row '''

    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
