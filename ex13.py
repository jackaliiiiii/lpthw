from sys import argv

script, first, second, third = argv

decision = raw_input("Are you sure you want to print them?(1 for yes/2)")

int(decision)
if decision == "1":
    print "The script is called:", script
    print "Your first variable is:", first
    print "Your second variable is:", second
    print "Your third variable is:", third
else:
    print "Thanks for your attendence."
