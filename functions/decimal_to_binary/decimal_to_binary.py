def decimal_to_binary(n):
    a = ""
    if n==0:
        return "0"
    while n>0:
        b = n%2
        a = str(b) + a
        n //= 2 
    return a