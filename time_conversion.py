#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    #[06:32:45PM]
    items = s.split(":")
    if items[2][2:4] == "PM":
        if items[0] == "12":
            return str("12" +":"+items[1] + ":" +items[2][:2])
        else:
            #eger pm se saate 12 ekleyip pm i silip return edicez
            hour = int(items[0]) + 12
            hour = str(hour)
            final = str(hour + ":" + items[1] + ":" + items[2][:2])
            return final
    else:
        if items[0] == "12":
            return str("00" +":"+items[1] + ":" +items[2][:2])
        else:
            #AM ise ayni sekilde return edicez
            return str(items[0] +":"+items[1] + ":" +items[2][:2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
