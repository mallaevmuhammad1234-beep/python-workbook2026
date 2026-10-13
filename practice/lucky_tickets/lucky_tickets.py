
def is_lucky(tic):
    tic=str(tic)
    a = int(tic[0])+int(tic[1])+int(tic[2])
    b = int(tic[3])+int(tic[4])+int(tic[5])
    if a == b:
        return True
    else :
        return False
x = int(input())
y = int(input())
d = 0
if 100000<=x<=y<=999999:
    for i in range(x,y+1):
        if is_lucky(i)==True:
            d+=1
        else :
            d = d 
print(d)
