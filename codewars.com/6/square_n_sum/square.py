#!/usr/bin/env python3

def squareSum(numbers):
    return sum(x**2 for x in numbers)

if __name__ == "__main__":
    print(squareSum([0, 3, 4, 5]))
