# -*- coding=utf-8 -*-
import itertools
# import timeit
import time

begin = time.clock()

list1 = []
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def notlarger(*args):

    # for i in args:
    #     list1.append(i)
    # thresh = list1.pop()
    # num = list1.pop()
    arg1, num, thresh = args
    for i in range(1, arg1 +1):
        list1.append(i)

    print list1

    # thresh = raw_input('Please input the threshold you want: ')
    iter = list(itertools.permutations(list1, arg1))

    sum = 0
    count = []

    for i in iter:
        perm = list(i)
        # print perm
        count1 = 0
        if perm[0] != 1:
            continue
        for x in range(0, num - 1):
            perm.append(perm[x])
            # perm.append(perm[1])
        for index in range(0, arg1):
            sumnum = 0
            for r in range(0, num):
                sumnum += perm[index + r]
                # print "perm[index] is: %d" %perm[index + r]
                # print sumnum
                # print perm
            if sumnum > thresh:
                # if perm[index] + perm[index + 1] + perm[index + 2] > thresh:
                count1 += 1
                # print count1
                # if count > 3:
                #     break
        # print count1
        if count1 > 3:
            continue
        # del perm[10, 11]
        for x in range(0, num -1):
            perm.pop()
        count.append(count1)
        sum += 1
        print perm
    print "The total number of case not bigger than 15 is: %d" % sum

# end = time.clock()
#
# print type(end)
# print "Running time is: %s" %(end - begin)
# print "Running time is: %d" %(end - begin)
# print "Running time is: %.3f" %(end - begin)
# print "Running time is: %r" %(end - begin)
#
# duration = round((end - begin), 3)
# print duration

notlarger(10, 3, 15)

'''

notlarger(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15)

# timeit.timeit("sum(range(100))")

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# iter = itertools.permutations(list1, 10)
#
# sum = 0
# for i in list(iter):
#     perm = list(i)
#     count = 0
#     if perm[0] != 1:
#         continue
#     perm.append(perm[0])
#     perm.append(perm[1])
#     for index in range(0, 10):
#         if perm[index] + perm[index + 1] + perm[index + 2] < 16:
#             count = count + 1
#         if count > 1:
#             break
#     if count > 1:
#         continue
#     perm.pop()
#     perm.pop()
#     sum += 1
#     print perm
# print "The total number of case larger than 15 is: %d" %sum
'''
