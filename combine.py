#!/bin/python3
import subprocess
import sys
from decimal import *
from itertools import product, accumulate, filterfalse

def isclose(a, b, rel_tol=1e-10, abs_tol=4.94065645841245644177e-323):
    return abs(a-b) <= max(Decimal(rel_tol) * max(abs(a), abs(b)), Decimal(abs_tol))

def mean(l):
    return sum(l)/len(l)

results = []

getcontext().prec = 6000

results.append(subprocess.run(["./uwe"] +  sys.argv[1:], capture_output=True))
results.append(subprocess.run(["./erik"] +  sys.argv[1:], capture_output=True))
results.append(subprocess.run(["./uwe2"] +  sys.argv[1:], capture_output=True))
results.append(subprocess.run(["./brandon"] +  sys.argv[1:], capture_output=True))

results = [Decimal(r.stdout.decode()) for r in results]

sorted_results = results.copy()
sorted_results.sort()

if isclose(sorted_results[0], sorted_results[-1]):
    print(f'{mean(sorted_results):.18e}')
elif isclose(sorted_results[1], sorted_results[-1]):
    print(f'Error (1 Wert falsch): {sorted_results[0]:.18e}')
    print(f'{mean(sorted_results[1:]):.18e}')
elif isclose(sorted_results[0], sorted_results[-2]):
    print(f'Error (1 Wert falsch): {sorted_results[-1]:.18e}')
    print(f'{mean(sorted_results[:-1]):.18e}')
else:
    print('Mehrere Fehler aufgetreten')
    print('Sicherer Zustand')
