def is_palindrome(s):
    a = str(s)
    b = len(a)
    for i in range(b // 2):
        if a[i] != a[b - i - 1]:
            return False
    return True