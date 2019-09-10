# import math :
# math module(library) 가져온다

from math import pi
# math module에서 pi만 가져온다

def circle(x):
    return pi * x * x

if __name__ == '__main__' :
    print('반지름 : %f' % circle(3))