rd = 90
sd = [1, 10, 25, 35, 60]


# Python program to find if there are 
# two elements wtih given sum 
# function to check for the given sum 
# in the array 
def printPairs(arr, arr_size, sum): 
    # Create an empty hash set 
    s = set() 
    for i in range(0,arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            print ("Pair with the given sum is", arr[i], "and", temp) 
        s.add(arr[i]) 

# printPairs(sd, len(sd), 60)


# a1 = [[1, 8], [2, 7], [3, 14]]
# a2 = [[1, 5], [2, 10], [3, 14]]
a1 = [[1, 8], [2, 15], [3, 9]]
a2 = [[1, 8], [2, 11], [3, 12]]

expect = 20

d1 = dict()
d2 = dict()
for e in a1:
    d1[e[1]] = e[0]

for e in a2:
    d2[e[1]] = e[0]


def findClosest(a1, a2, num):
    d1 = dict()
    d2 = dict()
    for e in a1:
        d1[e[1]] = e[0]

    for e in a2:
        d2[e[1]] = e[0]


    diff = 0x99999
    l = 0
    r = len(a2) - 1
    while l < len(a1) and r > 0:
        if num - (a1[l][1] + a2[r][1]) < 0:
            r -= 1
            continue

        if num - (a1[l][1] + a2[r][1]) < diff:
            diff = num - (a1[l][1] + a2[r][1])
        else:
            l += 1
    return a1[l][0], a2[r][0]

ret = findClosest(a1, a2, 20)
print ret
