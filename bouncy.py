def is_bouncy(number):
    asc = 0
    desc = 0
    for i in range(len(number) - 1):
        if (number[i] <= number[i+1]):
            asc += 1
        if (number[i] >= number[i+1]):
            desc += 1         
    if (asc == len(number) - 1):
        # increasing number
	    return False
    elif (desc == (len(number) - 1)):
        # decreasing number
	    return False    	
    else:
        # bouncy number
     	return True
    
def search():
    ini = 1
    bouncy = 0
    tot = 1
    while True:
        if is_bouncy(str(ini)):
            bouncy += 1
        if (bouncy/tot >= 0.99):
            break
        tot += 1    
        ini += 1
    return ini

print('The least number for which the proportion of bouncy numbers is exactly 99% is:', search())