from binary_adder import binary_add
from helpers import *

def booth_multiplier(q, m, n):
    a = '0' * len(q)
    y = '0'  # Qn-1 value taken as y here
    m_c = compliment(m)
    x = a + q + y
    
    check = x[-2:]
    if check == '00' or check == '11':
        x = right_shift(x)

    print(x)
    # while n > 0:
    #     # x = a + q + y

    #     if x[-2:] == '00' or x[-2:] == '11':
    #         x = right_shift(x)
    #     elif x[-2:] == '10':
    #         a = binary_add(x[:4], m)
    #         x = right_shift(x)
    #     elif x[-2:] == '01':
    #         a = binary_add(a, m_c)
    #         x = right_shift(x)
    #     print(x)
    #     n -= 1
        
    return a, x

booth_multiplier('01011010', '10', 8)

