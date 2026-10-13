def is_int(s):
    if s == "":
        return False
    elif s[0]=='-' or s[0]=='+':
        s = s[1:]
    if s.isdigit()==True:
        return True
    else:
        return False
