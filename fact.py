input=raw_input("Enter a number for factoriaal: ")
#Taking input from user

number=int(input)

#Initialising variables
fact=1

#while loop
i=1
while i<number:	
	fact=fact*number
	number=number-1

#printing the value of factorial
print(" Factorial is ", fact)

