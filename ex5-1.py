def dutch_flag(a, i):
    if not a:
        return

    a[i], a[-1] = a[-1], a[i]
    pivot = len(a) - 2
    lo = 0
    hi = len(a) - 2

    while lo <= hi:
        if a[lo] < a[-1]:
            lo += 1
        elif a[lo] > a[-1]:
            a[hi], a[lo] = a[lo], a[hi]
            hi -= 1 
        else:
            a[pivot], a[lo] = a[lo], a[pivot]
            pivot -= 1

            while pivot < hi:
                hi -= 1

    for idx in range(pivot + 1, len(a)):
        a[lo], a[idx] = a[idx], a[lo]
        lo += 1


a = [0, 1, 2, 0, 2, 1, 1]
b = a.copy()
dutch_flag(a, 3)
print(a)
dutch_flag(b, 2)
print(b)

c = [1, 1, 1, 1, 1, 2, 0]
dutch_flag(c, 0)
print(c)
