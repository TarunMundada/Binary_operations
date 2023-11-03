from binary_adder import binary_add

def compliment(a):
    inverse = ''
    for digit in a:
        if digit == "1":
            inverse += "0"
        else: inverse += "1"
    
    compliment = binary_add(inverse,'1')
    return compliment

def right_shift(a):
    shifted = '0' + a
    shifted = shifted[:-1]
    return shifted

def bin_to_dec(a) :
    x = int(a,2)
    return x

def dec_to_bin(a):
    x = bin(a).replace('0b', '')
    return x
