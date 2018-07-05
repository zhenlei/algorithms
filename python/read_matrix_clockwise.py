#!/usr/bin/env python3

"""
this program is used to read the two demisional array (matrix) in clockwise, in this example, it's
2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""

aa = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

h = len(aa)
l = len(aa[0])

# start from lenght, which means row
loopl = 1
#reverse and read row
looplr = 0
# read in height, which means column
looph = 0
#reverse and read column
loophr = 0
#length counter
lcount = 0
#height counter
hcount = 0
i = 0
# init j to -1, as initial value need add 1
j = -1

# total number of elements, if not use counter, you need mark every element which has been read.
counter=sum([len(line) for line in aa])

while (counter > 0):
    if (loopl == 1):
        for j in range(j+1, l-lcount, 1):
            print(aa[i][j])
            counter -=1
            if(j == l - lcount -1):
                looph = 1
                loopl = 0

    if (looplr == 1):
        for j in range(j-1, lcount -1, -1):
            print(aa[i][j])
            counter -=1
            if (j == lcount):
                loophr = 1
                looplr = 0
                lcount +=1
                hcount +=1

    if (loophr == 1):
        for i in range(i-1, hcount -1, -1):
            print(aa[i][j])
            counter -=1
            if (i == hcount):
                loopl = 1
                loophr = 0

    if (looph == 1):
        for i in range(i+1, h-hcount, 1):
            print(aa[i][j])
            counter -=1
            if (i == h-hcount -1):
                looplr = 1
                looph = 0
