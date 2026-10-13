def to_base(n, base):
    a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    if n==0:
        return "0"
    while n>0:
        b = n%base
        res = a[b] + res
        n//=base
    return res