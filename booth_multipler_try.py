def booth_multiplication(multiplicand, multiplier):
    # Determine the number of bits for the multiplicand and multiplier
    n = len(multiplicand)
    assert n == len(multiplier), "Multiplicand and multiplier must have the same number of bits"

    # Initialize variables for the algorithm
    product = [0] * (2 * n)
    accumulator = [0] * (n + 1)
    complement_multiplier = [1] if multiplier[-1] == 0 else [-1]

    for i in range(n):
        # Check if the last two bits of the multiplier are 10 or 01
        if multiplier[-1] == 0 and complement_multiplier[0] == -1:
            # Perform A = A - M
            for j in range(n):
                accumulator[j] += multiplicand[j]

        elif multiplier[-1] == 1 and complement_multiplier[0] == 1:
            # Perform A = A + M
            for j in range(n):
                accumulator[j] -= multiplicand[j]

        # Right shift the accumulator and the multiplier
        accumulator, complement_multiplier, multiplier = [accumulator[-1]] + accumulator[:-1], [complement_multiplier[-1]] + complement_multiplier[:-1], [multiplier[-1]] + multiplier[:-1]

        # Update the product
        for j in range(n):
            product[j] = accumulator[j]

    return product[:n]

# Example usage
multiplicand = [1, 0, 0, 1]  # 9 in binary (1001)
multiplier = [1, 1, 0, 1]    # 13 in binary (1101)

result = booth_multiplication(multiplicand, multiplier)
print("Multiplicand:", multiplicand)
print("Multiplier:", multiplier)
print("Product:", result)
