#!/usr/bin/python3
import sys
sum = 0
for i in sys.argv[1:]:
    sum = sum + int(i)
print("{}".format(sum))
