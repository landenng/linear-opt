import math 
import time

def f(x: float) -> float: return x ** 2 / 10 - 2 * math.sin(x)

def check_pos(x1: float, x2: float) -> str:
    if x2 < x1: return 'right'
    return ''

def update_interior(xl: float, xu: float) -> tuple[float, float]:
    d = ((math.sqrt(5) - 1) / 2) * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    return x1, x2

def find_max(xl: float, xu: float, x1: float, x2: float, label: str) -> tuple[float, float, float]:
    fx1, fx2 = f(x1), f(x2)
    if fx2 > fx1 and label == 'right':
        xl, xu = xl, x1
        x1, x2 = update_interior(xl, xu)
        xopt = x2
    else:
        xl, xu = x2, xu
        x1, x2 = update_interior(xl, xu)
        xopt = x1
    return xl, xu, xopt

def find_min(xl: float, xu: float, x1: float, x2: float, label: str) -> tuple[float, float, float]:
    fx1, fx2 = f(x1), f(x2)
    if fx2 > fx1 and label == 'right':
        xl, xu = x2, xu
        x1, x2 = update_interior(xl, xu)
        xopt = x1
    else:
        xl, xu = xl, x1
        x1, x2 = update_interior(xl, xu)
        xopt = x2
    return xl, xu, xopt

def golden(xl: float, xu: float, mode: str, et: float) -> None:
    it, e = 0, 1
    while e >= et:
        x1, x2 = update_interior(xl, xu)
        label = check_pos(x1, x2)
        if mode == 'max': new_boundary = find_max(xl, xu, x1, x2, label)
        elif mode == 'min': new_boundary = find_min(xl, xu, x1, x2, label)
        else:
            print('please define min/max mode')
            break
        [xl, xu, xopt] = new_boundary
        it += 1
        R = (math.sqrt(5) - 1) / 2 # golden ratio
        e = ((1 - R) * (abs((xu - xl) / xopt))) * 100 # error term
        if it == 5:
            print('############################################ ANSWER TO 1 AND 2 ############################################')
            print()
            print('Iteration: ', it)
            print(f'x = {xopt}') 
            print(f'f(x) = {f(xopt)}')
            print(f'e = {e} %')
            print()
            print('############################################ ANSWER TO 1 AND 2 ############################################')
            print()
        else:
            print('Iteration: ', it)
            print(f'x = {xopt}, f(x) = {f(xopt)}')
            print('error: ', e)
            print()
        time.sleep(0.50)

##############################################################
####################### MAIN #################################
##############################################################

golden(0, 4, 'min', 0.05)
