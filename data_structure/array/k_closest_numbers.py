#!/usr/bin/env python3

"""
  Given an unsorted array and two numbers x and k, find k closest values to x.

  Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3
  Output : 4 6 7
  Three closest values of x are 4, 6 and 7.

  Input : arr[] = {-10, -50, 20, 17, 80}, x = 20, k = 2
  Output : 17, 20

  refer to [[https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/]]
"""

from __future__ import print_function
import math
from queue import PriorityQueue

class Element:
    def __init__(self, p, v, desc=None):
        self.pri = p
        self.val = v
        self.desc = desc

    def __cmp__(self, e):
        return cmp(self.pri, e.pri)

    def __lt__(self, e):
        return self.pri < e.pri

    def __str__(self):
        return '%s:%s' % (self.pri, self.val)

def findKclosset(arr, x, k):
    pq = PriorityQueue()
    for i in range(k):
        pq.put(Element(-abs(arr[i] - x), i))

    print(pq.__dict__)
    for i in range(k, len(arr)):
        e = pq.get()

        o = Element(-abs(arr[i] - x), i)
        if o > e:
            pq.put(o)
        else:
            pq.put(e)

    while not pq.empty():
        i = pq.get()
        print('{}'.format(arr[i.val]))


arr = [ 10, 2, 14, 4, 7, 6 ]

findKclosset(arr, 5, 3)
