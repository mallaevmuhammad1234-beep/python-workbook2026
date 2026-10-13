import math

def quadratic_roots(a,b,c):
    dis = b*b - 4*a*c 
    if dis<0:
        return None
    elif dis==0:
        return -b/(2*a)
    elif dis>0:
        x1 = (-b + math.sqrt(dis)) / (2*a)
        x2 = (-b - math.sqrt(dis)) / (2*a)
        return x1,x2