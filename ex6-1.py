def convert_str_to_int(s):
    offset = 1
    total = 0

    digs = '0123456789'
    digs_ints = list(range(10))
    vals = dict(zip(digs, digs_ints))

    for c in reversed(s):
        total += vals[c] * offset
        offset *= 10
    return total


from collections import deque
def convert_int_to_str(n):
    if n == 0:
        return '0'
    
    negative = n < 0
    if negative:
        n *= -1

    d = deque()

    digs = '0123456789'
    digs_ints = list(range(10))
    vals = dict(zip(digs_ints, digs))

    while n > 0:
        d.appendleft(vals[n % 10])
        n //= 10

    if negative:
        d.appendleft('-')

    return ''.join(d)

n = 123
print(convert_int_to_str(n))
s = '123'
print(convert_str_to_int(s))