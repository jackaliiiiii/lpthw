# -*- coding=utf-8 -*-
import itertools
# import timeit
import time

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter = itertools.permutations(list1, 10)

sum = 0
for i in list(iter):
    perm = list(i)
    count = 0
    if perm[0] != 1:
        continue
    perm.append(perm[0])
    perm.append(perm[1])
    for index in range(0, 10):
        if perm[index] + perm[index + 1] + perm[index + 2] > 15:
            count = count + 1
        if count > 3:
            break
    if count > 3:
        continue
    perm.pop()
    perm.pop()
    sum += 1
    print perm
print "The total number of case larger than 15 is: %d" %sum
