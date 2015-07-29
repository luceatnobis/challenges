#!/usr/bin/env python
# http://www.cstutoringcenter.com/problems/problems.php?id=37

import time

cubes = set()
squares = set()

def fill_sets():
	target = 100000
	i=1
	q=0
	while q < target:
            q = i**2
            squares.add(q)
            c = i**3
            if c<target: cubes.add(i**3)
            i+=1

def check(n):
	for i in cubes:
		if (n-i) in squares: 
			return True
	return False

def main():
	sum = 0
	for x in xrange(1,100001):
		if check(x):
			sum+=x

	print sum

if __name__ == "__main__":
	t1 = time.time()
	fill_sets()
	main()
	t2 = time.time()
	print "time in sec:",(t2-t1)
