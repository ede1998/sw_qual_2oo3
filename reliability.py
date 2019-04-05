#!/bin/python3

import sys
from decimal import *
from functools import reduce

getcontext().prec = 6000
def calc_R_i(lambdas, t=87600):
    return [Decimal(-t*l).exp() for l in lambdas]

def calc_R_p(R_is):
    return Decimal(1) - reduce(lambda x,y: x*y, [1 - R_i for R_i in R_is])

R_i = calc_R_i([Decimal(i) for i in sys.argv[1:]])
R_p = calc_R_p(R_i)

print(f'{R_p:.18e}')
