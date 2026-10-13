def caesar_cipher(text, num):
    res = ""
    for char in text:
        if char>='a' and char<='z':
            res += chr((ord(char)-ord('a')+num)%26+ord('a'))
        elif char>="A" and char<='Z':
            res += chr((ord(char)-ord('A')+num)%26+ord('A'))
        else:
            res += char
    return res