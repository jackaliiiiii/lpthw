print True and True, "\n------True"
print False and True, "\n------false"
print 1 == 1 and 2 == 1, "\n------false"
print "test" == "test", "\n------True"
print 1 == 1 or 2 != 1, "\n------True"
print True and 1 == 1, "\n------True"
print False and 0 != 0, "\n------False"
print True or 1 == 1, "\n------True"
print "test" == "testing", "\n------false"
print 1 != 0 and 2 == 1, "\n------false"
print "test" != "testing", "\n------True"
print "test" == 1, "\n------false"
print not (True and False), "\n------True"
print not (1 == 1 and 0 != 1), "\n------false"
print not (10 == 1 or 1000 == 1000), "\n------false"
print not (1 != 10 or 3 == 4), "\n------false"
print not ("testing" == "testing" and "Zed" == "Cool Guy"), "\n------True"
print 1 == 1 and (not ("testing" == 1 or 1 == 0)), "\n------True"
print "chunky" == "bacon" and (not (3 == 4 or 3 == 3)), "\n------false"
print 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")), "\n------false"

print "test" and "test"