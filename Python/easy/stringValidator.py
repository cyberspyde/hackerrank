if __name__ == '__main__':
    s = input()
    line1 = False
    line2 = False
    line3 = False
    line4 = False
    line5 = False
    for k in s:
        if k.isalnum():
            line1 = True
        if k.isalpha():
            line2 = True
        if k.isdigit():
            line3 = True
        if k.islower():
            line4 = True
        if k.isupper():
            line5 = True
            
    print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")