'''
worst case:
    space complexity o(n^2)
    time complexity o(n)

best case:
    space complexity o(logn)
    time complexity o(nlogn)
'''


def quick_sort(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)


def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
