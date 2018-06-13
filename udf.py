#!/usr/bin/python2

#Creating a user defined function
def factorial(num):
	if num==1:
		return num
	else:
		return num*factorial(num-1)

#Taking a numer as input from user
num =input("Enter number ")

if num<0:
	print("Fact can't be a number")
elif num==0:
	print("Fact is 1")
else:
	print("Factorial of given number is ",factorial(num))




