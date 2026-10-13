def password(length):
    import random

    a="abcdefskmkmshpolaxzAGSHXNBVCTEIPLC15273404056082872@$!%&(_*&$@!!()+/*-)"
    res=""
    for i in range(1,length+1):
        b = random.randint(0,len(a)-1)
        res += a[b]
    return res