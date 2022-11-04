# brute force: O(m) complexity where len(words) = m
def parity(words):
    def single_parity(x):
        count = 0
        while x:
            if x & 1:
                count += 1
            x >>= 1
        return count
    
    return [single_parity(x) for x in words]

# can be memoized by storing previously computed values

def single_parity2(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

def compute_table(n):
    return [single_parity2(i) for i in range(n)]

MASK = 2**17 - 1
def parity2(words):
    table = compute_table(2**16)
    parities = []
    for word in words:
        p = table[word >> 48] + table[(word >> 32) & MASK] + table[(word >> 16) & MASK] + table[word & MASK]
        parities.append(p % 2)
            
    return parities
        

def prop_rightmost(x):
    return x | (x - 1)

def mod2(x):
    return x & 0x1

def pwr_of_2(x):
    return (x & (x - 1)) == 0