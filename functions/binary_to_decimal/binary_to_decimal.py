def binary_to_decimal(binary):
    dec = 0
    length = len(binary)
    for i in range (length):
        b = int(binary[length-i-1])
        dec += b * (2 ** i)
    return dec