# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_list(args):
    list =[]
    for i in range(0, args):
        list.append(i)
    print list

# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothing."

print_two("Jack","Li")
print_two_again("Jack","Li")
print_one("Jack~")
print_none()
print_list(10)
