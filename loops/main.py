#!/usr/bin/env python3

"""
Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i squared.

Example:
n = 3

The list of non-negative integers that are less than n ==3 is [0, 1 , 2] . Print the square of each number on a separate line.
"""

def print_squares(n):
    for i in range(n):
        print(i * i)


if __name__ == '__main__':
    n = int(input())

    print_squares(n)
