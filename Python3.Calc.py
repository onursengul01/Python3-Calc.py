import os
import pyfiglet

class Calculator:
	def __init__(self):
		pass

	def Menu(self):
		result = pyfiglet.figlet_format("Calculator")
		print(result)  
		while True:
			print("1) Divide")
			print("2) Multiply")
			print("3) Addition")
			print("4) Subtraction")

			options = input("Choose: ")

			if options == "1":
				return c.Divide()

			if options == "":
				os.system("cls")
				return c.Menu()

			if options == "2":
				return c.Multiply()
			if options == "3":
				return c.Addition()

			if options == "4":
				return c.Subtraction()
			if options == "exit":
				exit()
	def Divide(self):
		global div
		global div2
		try:
			div = int(input("Enter a number to divde: "))
		except(ValueError):
			print("Please enter a number")
			return c.Divide()
		try:
			div2 = int(input("Enter a second number to divide: "))
		except(ValueError):
			print("Please enter a number")
			return c.Divide()
		print(div, " / ", div2, " = ", div/div2+0.5)
		return c.Menu()

	def Multiply(self):
		global multi 
		global multi2

		try:
			multi = int(input("Enter a number to multiply: "))
		except(ValueError):
			print("Please enter a number")
			return c.Multiply()
		try:
			multi2 = int(input("Enter a second number to multiply: "))
		except(ValueError):
			print("Please enter a number")
			return c.Multiply()
		print(multi, " * ", multi2, " = ", multi*multi2)
		return c.Menu()
	
	def Addition(self):
		global add 
		
		try:
			add = int(input("Enter a number to add: "))
			
		except(ValueError):
			print("Please enter a number")
			return c.Addition()

		try:
			add2 = int(input("Enter a second number to add: "))
		except(ValueError):
			print("Please enter number")
			return c.Addition()

		print(add, " + ", add2, " = ", add+add2)
		return c.Menu()



	def Subtraction(self):
		global add 
		
		try:
			sub = int(input("Enter a number to subtract: "))
			
		except(ValueError):
			print("Please enter a number")
			return c.Subtraction()

		try:
			sub2 = int(input("Enter a second number to subtract: "))
		except(ValueError):
			print("Please enter number")
			return c.Subtraction()

		print(sub, " -", sub2, " = ", sub-sub2)
		return c.Menu()	



c = Calculator()
c.Menu()
c.Divide()
c.Multiply()
c.Addition()
c.Subtraction()
