#!/usr/bin/env python
import itertools

if __name__ == "__main__":

    thresh = 15
    l = []
    for i in range(1,11):
        l.append(i)

    print l

    pl = list(itertools.permutations(l))

    l_count = []
    count = 0
    sum = 0
    min = 999
    max = 0
    count_max = 0
    for i in range(len(pl)):
        for k in range(10):
            sum = pl[i][k] + pl[i][(k+1)%10] + pl[i][(k+2)%10]
            if sum > 15:
                count = count + 1

        l_count.append(count)
        if count <= min:
            min = count
        if count > max:
            max = count
        count = 0

    m = 0
    n = 0
    for i in range(len(pl)):
        if l_count[i] == min:
            if pl[i][0] == 1:
                m = m + 1
                print pl[i]
        if l_count[i] == max:
            n = n + 1


    print "min=",min
    print "total number=",m

    print "max=",max
    print "total max number = ",n
