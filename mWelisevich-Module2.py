# Mick Welisevich
# Fiber Optic Calculator
# ver 1.0 
# 21 MAR 21

def findPrice():
	answer = "n"
	while answer.upper() != "Y":
		compName = input("What is your company name? ")
		answer = input("Is " + str(compName) + " correct? y/n ")
	answer = "n"
	while answer.upper() != "Y":
		reqLen = float(input("How many feet of Fiber Optic Cable does your company need? "))
		answer = input("Is " + str(reqLen) + " correct? y/n ")
	price = reqLen * 0.87
	print(str(compName) + ", your quote is $" + str(price) + " for "
		+str(reqLen) + "ft. of Fiber Optic. Thank you and have a nice day.")

findPrice()

