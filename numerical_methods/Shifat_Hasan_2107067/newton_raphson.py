import numpy as np
import numerical_methods as nm


def newton_raphson(f: str, df: str):
    pass


def solve_using_newton_raphson():
    f = input("Enter the function  :  ")
    df = input("Enter the derivative:  ")

    roots = newton_raphson(f, df)

    print(roots)
