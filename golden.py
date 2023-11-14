import numpy as np
import time

def f(x):
    return x ** 2 / 10 - 2 * np.sin(x)

def check_pos(x1: float, x2: float):
    if x2 < x1:
        label = "right"
    else:
        label = ""
    return label

def update_interior(xl: float, xu: float):
    d = ((np.sqrt(5) - 1) / 2) * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    return x1, x2

def find_max(xl: float, xu: float, x1: float, x2: float, label: str):
    fx1 = f(x1)
    fx2 = f(x2)

    if fx2 > fx1 and label == "right":
        xl = xl
        xu = x1

        new_x = update_interior(xl, xu)

        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x2
    else:
        xl = x2
        xu = xu

        new_x = update_interior(xl, xu)

        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x1
    return xl, xu, xopt

def find_min(xl: float, xu: float, x1: float, x2: float, label: str):
    fx1 = f(x1)
    fx2 = f(x2)

    if fx2 > fx1 and label == "right":
        xl = x2
        xu = xu

        new_x = update_interior(xl, xu)

        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x1
    else:
        xl = xl
        xu = x1

        new_x = update_interior(xl, xu)

        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x2
    return xl, xu, xopt

def golden(xl: float, xu: float, mode: str, et: float):
    it = 0
    e = 1

    while e >= et:
        new_x = update_interior(xl, xu)
        x1    = new_x[0]
        x2    = new_x[1]
        label = check_pos(x1, x2)

        if mode == "max":
            new_boundary = find_max(xl, xu, x1, x2, label)
        elif mode == "min":
            new_boundary = find_min(xl, xu, x1, x2, label)
        else:
            print("please define min/max mode")
            break

        xl   = new_boundary[0]
        xu   = new_boundary[1]
        xopt = new_boundary[2]

        it += 1


        R = (np.sqrt(5) - 1) / 2 # golden ratio

        e = ((1 - R) * (abs((xu - xl) / xopt))) * 100 # error term


        if it == 5:
            print("############################################ ANSWER TO 1 AND 2 ############################################")
            print()
            print("Iteration: ", it)
            print(f"x = {xopt}") 
            print(f"f(x) = {f(xopt)}")
            print(f"e = {e} %")
            print()
            print("############################################ ANSWER TO 1 AND 2 ############################################")
            print()
        else:
            print("Iteration: ", it)
            print(f"x = {xopt}, f(x) = {f(xopt)}")
            print("error: ", e)
            print()


        time.sleep(0.50)

##############################################################
####################### MAIN #################################
##############################################################

golden(0, 4, "min", 0.05)
