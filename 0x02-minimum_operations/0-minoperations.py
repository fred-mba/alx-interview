#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    if n <= 1:
        return 0

    operations, factor = 0, 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
            factor -= 1
        factor += 1
    return operations
