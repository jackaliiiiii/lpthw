numbers = []

def build_list(max):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

def build_list1(max):
    for i in range(0, max):
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

build_list1(int(raw_input("Input the max value in list:")))

print "The numbers: "

for num in numbers:
    print num
