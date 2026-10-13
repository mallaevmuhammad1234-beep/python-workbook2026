def luhn_sum(number):
    a = number
    b = len(number) 
    sum = 0
    for i in range(1,b+1):
        if i%2==0:
            digit=int(number[b-i])*2
            if digit>9:
                digit-=9
            sum+=digit
        else:
            sum+=int(number[b-i])

def is_valid_card(number):
    a = len(number)
    if number.isdigit()==True and a >= 2 and luhn_sum(number)%10==0:
        return True
    else:
        return False

def check_digit(partial):
    a = len(partial)
    b = luhn_sum(partial)
    for i in range (0,10):
        if (b+i)%10==0:
            partial=partial+str(i)
    return partial
