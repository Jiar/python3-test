#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def normalize(name):
	return name.lower().capitalize()

	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	return reduce(lambda x, y: x * y, L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('3 * 5 * 7 * 9 =', reduce(lambda x, y: x * y, [3, 5, 7, 9]))




