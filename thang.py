def checkPassword(password):
    number = [x for x in range(0, len(password)) if unicode(password[x], 'utf-8').isnumeric() == True]
    u = [x for x in range(0, len(password)) if password[x].isupper() == True]
    l = [x for x in range(0, len(password)) if password[x].islower() == True]
    if (len(number) * len(u) * len(l)) > 0:
        return True
    else:
        return False

print checkPassword("sHlatt1")
print checkPassword("sHlatt")
print checkPassword("shlatt1")
print checkPassword("ROACH1")

def ratePassword(password):
    rating = 0
    number = [x for x in range(0, len(password)) if unicode(password[x], 'utf-8').isnumeric() == True]
    u = [x for x in range(0, len(password)) if password[x].isupper() == True]
    l = [x for x in range(0, len(password)) if password[x].islower() == True]
    char = [x for x in range(0, len(password)) if password[x] in "~!@#$%^&*"]
    if len(l) > 0:
        rating += 3
    if len(u) > 0:
        rating += 2
    if len(number) > 0:
        rating += 2
    if len(char) > 0:
        rating += 3
    
    return rating

print ratePassword("scHlatt#1") #10
print ratePassword("ROACH1") #4
print ratePassword("scHlatt1") #7
print ratePassword("schlatt1") #5
print ratePassword("scHlatt#") #8
        
