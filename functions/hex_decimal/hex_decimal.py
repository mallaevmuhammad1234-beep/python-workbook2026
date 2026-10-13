def hex_decimal(hex_str):
    digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    decimal = 0

    for i in range(len(hex_str)):
        for j in range(16):
            if hex_str[i] == digits[j]:
                decimal = decimal * 16 + j
                break

    return decimal