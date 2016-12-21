def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtact(a, b):
    print "SUBTACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(int(raw_input("Former age:")), int(raw_input("How many years past:")))
height = subtact(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, height, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is the puzzle."

what = add(age, subtact(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
