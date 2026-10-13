def below_100(n):
    x ="ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety" 
    y ="one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"

    if n%10==0:
        a = n // 10
        return x[a - 1]
    elif n < 20:
        return y[n - 1]
    elif n>20:
        a = n // 10
        b = n % 10
        return x[a - 1] + " " + y[b - 1]
def below_1000(n):
    hund="hundred", "two hundred", "three hundred" , "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred" 
    z = n%100
    v = n//100
    return hund[z - 1] + " " + below_100(v)
a = int(input())
if a<100:
    print(f"{below_100(a)}")
elif a<1000 and a>99:
    print(f"{below_1000(a)}")

