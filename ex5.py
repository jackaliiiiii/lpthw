# -*- coding: utf-8 -*-
my_name = u'李钟麟'
my_age = 28 # not a lie
my_height = 187 #centimeters
my_weight = 187 # jin
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print my_name
print u'李钟麟'
print r'李钟麟' #%r is a very useful one. It's like saying "print this no matter what."
print u"“李钟麟”"
print "He's %d centimeters tall." % my_height
print "He's %d jin heavy." % my_weight
print "Acturally that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usurally %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
my_age, my_height, my_weight, my_age + my_height + my_weight
)
