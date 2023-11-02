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

print(right_shift('001111'))