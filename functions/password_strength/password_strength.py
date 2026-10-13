def password_strength(pwd):
    a=len(pwd)
    is_upper =False
    is_lower = False
    is_digit = False
    spec = False
    cnt =0
    sp="!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in pwd:
        if char.isupper():
            is_upper = True
        elif char.isdigit():
            is_digit = True
        elif char.islower():
            is_lower = True 
        elif char in sp:
            spec = True
    if is_upper == True:
        cnt += 1
    if is_lower == True:
        cnt += 1
    if is_digit == True:
        cnt += 1
    if spec == True:
        cnt += 1

    if a<8 or cnt == 1:
        return "weak"
    elif cnt >= 2 and a>=8 and a<12:
        return "medium"
    elif a>=12 and cnt >= 3:
        return "strong"