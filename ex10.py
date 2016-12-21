# -*- coding: utf-8 -*-
print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string
print "I am 6\'2\" tall."  # escape double-quote inside string
print 'I am 6''2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
\u李钟麟
\U李钟麟
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

print "%r"  %"\""
print "%r"  %"\'"

print "%s"  %"\""
print "%s"  %"\'"
