def isLeapYear(year):
    if (year % 400) == 0:
        return True
    elif(year % 100) == 0:
        return False    
    elif(year % 4) == 0:
        return True
    else:
        return False
#year = int(input("Year : "))
year = 1800

print(f"{year} is " + "Leap Year" if isLeapYear(year) else "Not a Leap Year")