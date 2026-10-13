def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
def classify(n):
    a = sum_of_divisors(n)
    if n == a:
        return "perfect"
    elif a>n:
        return "abundant"
    elif a<n:
        return "deficient"
x = int(input())
y = int(input())
per=0
abu=0
defi = 0
for i in range (x,y+1):
    cnt = classify(i)
    if cnt=="perfect":
        per+=1
    elif cnt=="abundant":
        abu+=1
    elif cnt=="deficient":
        defi+=1
    print(f"{i} is {cnt}")
print(f"Perfect: {per}, Abundant: {abu}, Deficient: {defi}")