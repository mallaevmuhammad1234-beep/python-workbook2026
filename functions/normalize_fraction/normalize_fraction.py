def normalize_fraction(numerator, denominator):
    gcd = 0
    if numerator==0:
        a = denominator
    elif denominator==0:
        a = numerator
    elif numerator > denominator:
        a = denominator
    elif numerator <= denominator:
        a = numerator 
    for i in range (1, a+1):
        if numerator%i==0 and denominator%i==0:
            gcd = i
    numerator = numerator//gcd
    denominator = denominator//gcd
    return numerator, denominator
