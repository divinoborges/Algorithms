import math


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0.0] * (n1 + 1)
    right = [0.0] * (n2 + 1)

    for i in range(n1):
        left[i] = a[p + i]

    for j in range(n2):
        right[j] = a[q + j + 1]

    left[n1] = math.inf
    right[n2] = math.inf

    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
