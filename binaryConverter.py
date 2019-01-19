def toBinary(n):
	if(n < 2):
		return str(n)
	else:
	    mod =  n % 2
	    floor = n // 2
	    return toBinary(floor) + str(mod)

print(toBinary(255))
