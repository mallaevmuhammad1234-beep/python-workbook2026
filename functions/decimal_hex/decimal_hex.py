def decimal_hex(n):
    a = "0123456789ABCDEF"
    res = ""
    if n==0:
        return '0'
    while n>0:
        b=n%16
        res=a[b]+res
        n//=16
    return res