#!/usr/bin/env python
from __future__ import division
from math import sqrt

x = 5
one = 0
three = 0
seven = 0
nine = 0
prime=[2,3]
while True:
	for number in prime:
		if x % number != 0:
			notprime = 0
			continue
		else:
			notprime = 1
			break
	if notprime == 0:
		xstring = list(str(x))
		if xstring[-1] == '1':
			one += 1
		elif xstring[-1] == '3':
			three += 1
		elif xstring[-1] == '7':
			seven += 1
		elif xstring[-1] == '9':
			nine += 1
		prime.append(x)
		print (x, len(prime), one, three, seven, nine, x/len(prime), len(prime)/x, (len(prime)/x)-(len(prime[:-1])/prime[-1]))
	x += 2
# sqrt(x), sqrt(len(prime)), sqrt(x)/sqrt(len(prime)),(sqrt(x)/sqrt(len(prime)))/(sqrt(x)/sqrt(len(prime)-1)), (sqrt(x)/sqrt(len(prime))) - (sqrt(x)/sqrt(len(prime)-1))