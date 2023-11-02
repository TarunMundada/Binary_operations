from binary_adder import binary_add
from helpers import *

def booth_multiplier(q, m, n):
    a = '0' * len(q)
    y = '0'  # Qn-1 value taken as y here
    m_c = compliment(m)
    x = a + q + y

    while n > 0:
        if x[-2:] == '00' or x[-2:] == '11':
            x = right_shift(x)
        elif x[-2:] == '10':
            a = binary_add(a, m)
            x = right_shift(x)
        elif x[-2:] == '01':
            a = binary_add(a, m_c)
            x = right_shift(x)

        n -= 1
        
        print(x)

    return a, x

booth_multiplier('1011', '1001', 4)

