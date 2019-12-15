import copy

def merge(arr, p, m, q):
    larr = []
    rarr = []

    larr = copy.deepcopy(arr[p:m])
    rarr = copy.deepcopy(arr[m+1:q])

    i = 0
    j = 0
    k = 0
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1

    while i < len(larr):
        arr[k] = larr[i]
        k += 1
        i += 1

    while j < len(rarr):
        arr[k] = rarr[j]
        k += 1
        j += 1

def partition(arr, p, q):
    if p >= q:
        return
    m = ( p + q ) // 2

    print 'p', p, 'm', m, 'q', q
    partition(arr, p, m)
    partition(arr, m+1, q)

    merge(arr, p, m, q)

arr = [3, 5, 10, 2, 20, 1, 33, 18]

partition(arr, 0, len(arr))
print arr
