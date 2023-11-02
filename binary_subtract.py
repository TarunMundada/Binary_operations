from binary_adder import binary_add
from helpers import compliment

def binary_sub(a,b):
    b_c = compliment(b)
    result = binary_add(a,b_c)
    return result