import os
import math


while True:
	def Home():
		print("$-----Welcome To Lobby-----$")
		print()
		print("You can enter [1] to divide")
		print("You can enter [2] to multiply")
		print("You can enter [3] to add")
		print("You can enter [4] to subtract")
		print("Would you like to see more calculater options: If u you can want enter [5]")
		print("You can type [help] to check more info about the program")
		options = input("1/2/3/4/5: ")

		if options == "1":
			def div_return():
				div = int(input("Enter your number to divide: "))
				div2 = int(input("Enter your second number to divide: "))
				print(div, "÷", div2, "=", div/div2)
				while True:
					add_more = input("Would you like to divide more: [yes] or [no]: ")
					if add_more == "yes":
						os.system("cls")
						while True:
							div3 = int(input("Enter your number to divide: "))
							div4 = int(input("Enter your second number to divide: "))
							print(div3, "÷", div4, "=", div3/div4)
							return div_return()
					if add_more == "no":
						os.system("cls")
						break
						Home()
					if add_more == "y":
						os.system("cls")
						return div_return()

					if add_more == "n":
						os.system("cls")
						break
						Home()						

			div_return()

		if options == "2":
			def multi_return():
				multi = int(input("Enter your number to multiply: "))
				multi2 = int(input("Enter your second number to multiply: "))
				print(multi, "x", multi2, "=", multi*multi2)
				while True:
					multi_more = input("Would you like to multiply more: [yes] or [no]: ")
					if multi_more == "yes":
						os.system("cls")
						while True:
							multi3 = int(input("Enter your number to multiply: "))
							multi4 = int(input("Enter your second number multiply: "))
							print(multi3, "x", multi4, "=", multi3*multi4)
							return multi_return()
					if multi_more == "no":
						os.system("cls")
						break
						Home()
					if multi_more == "y":
						os.system("cls")
						return multi_return()
					if multi_more == "n":
						os.system("cls")
						break
						Home()
			multi_return()

		if options == "3":
			def add_return():
				add = int(input("Enter your number to add: "))
				add2 = int(input("Enter your second number to add: "))
				print(add, "+", add2, "=", add+add2)
				while True:
					add_more2 = input("Would you like to add more: [yes] or [no]: ")
					if add_more2 == "yes":
						os.system("cls")
						while True:
							add3 = int(input("Enter your number to add: "))
							add4 = int(input("Enter your second number to add: "))
							print(add3, "+", add4, "=", add3+add4)
							return add_return()
					if add_more2 == "no":
						os.system("cls")
						break
						Home()

					if add_more2 == "y":
						os.system("cls")
						return add_return()

					if add_more2 == "n":
						os.system("cls")
						break
						Home()


			add_return()

		if options == "4":
			def  sub_return():
				sub = int(input("Enter your number to subtract: "))
				sub2 = int(input("Enter your second number to subtract: "))
				print(sub, "-", sub2, "=", sub-sub2)
				while True:
					sub_more = input("Would you like to subtract more: [yes] or [no]: ")
					if sub_more == "yes":
						os.system("cls")
						while True:
							sub3 = int(input("Enter your number to subtract: "))
							sub4 = int(input("Enter your second number to subtract: "))
							print(sub3, "-", sub4, "=", sub3-sub4)
							return sub_return()
					if sub_more == "no":
						os.system("cls")
						break
						Home()
					if sub_more == "y":
						os.system("cls")
						return sub_return()
			
					if sub_more == "n":
						os.system("cls")
						break
						Home()	

			sub_return()
		
		if options == "help":
			def Help_menu():
				os.system("cls")
				print("You can type 'cls' to clear")
				print("The program is in a while loop; it will repeat until you type 'exit'")
				print("This program works for windows system only.")
				while True:
					print()
					help_menu = input("Would you like to stay in the help menu: [yes] or [no]: ")
					if help_menu == "yes":
						return Help_menu()
					if help_menu == "no":
						os.system("cls")
						break
						Home()
					if help_menu == "y":
						return Help_menu()
					if help_menu == "n":
						os.system("cls")
						break
						Home()
			Help_menu()



			
		if options == "5":
			def more_options():
				os.system("cls")
				while True:

					print("You can enter '1' to Square root")
					print("You can enter '2' to Square cube")
					print("You can type 'help'")
					options2 = input("1/2: ")
					if options2 == "1":
						def sqaure_root_options():
							root = int(input("Enter your number to Square root: "))
							sqrt = root**(.5)
							print("Your answer is: ", sqrt)
							while True:
								root_menu = input("Would you like to keep Square root: [yes] or [no]: ")
								if root_menu == "yes":
									root2 = int(input("Enter your number to Square root: "))
									sqrt2 = root2**(.5)
									print("Your answer is: ", sqrt2)
									return sqaure_root_options()
								if root_menu == "no":
									os.system("cls")
									break
									more_options()
								if root_menu == "y":
									root3 = int(input("Enter your number to Square root: "))
									sqrt3 = root3**(.5)
									print("Your answer is: ", sqrt3)
									return sqaure_root_options()
								if root_menu == "n":
									os.system("cls")
									break
									more_options()

						sqaure_root_options()	


			
					if options2 == "2":
						def square_cube_options():
							cube_root = int(input("Enter your number to Cube root: "))
							cube_root2 = cube_root**(1. / 3)
							print("Your answer is: ", cube_root2)
							while True:
								cube_menu = input("Would you like to to keep Cube root: [yes] or [no]: ")
								if cube_menu == "yes":
									cube_root3 = int(input("Enter your number to Cube root: "))
									cube_root_total = cube_root3**(.5)
									print("Your answer is: ", cube_root3)
								if cube_menu == "y":
									return square_cube_options()
								if cube_menu == "no":
									os.system("cls")
									break
									square_cube_options()
								if cube_menu == "n":
									os.system("cls")
									break
									square_cube_options()
									

						square_cube_options()	
			




					if options2 == "help":
						def Help_menu2():
							os.system("cls")
							print("You can type 'cls' to clear")
							print("you can type 'lobby' or 'l' to go to main calcualter menu.")
							print("The program is in a while loop; it will the program will repeat until you type 'exit'")
							while True:
								print()
								help_menu = input("Would you like to stay in the help menu: [yes] or [no]: ")
								if help_menu == "yes":
									return Help_menu2()
								if help_menu == "no":
									os.system("cls")
									break
									more_options()
								if help_menu == "y":
									return Help_menu2()
								if help_menu == "n":
									os.system("cls")
									break
									more_options()
						Help_menu2()
			

					if options2 == "lobby":
						os.system("cls")
						break
						return Home()
					if options2 == "l":
						os.system("cls")
						break
						return Home()
					if options2 == "exit":
						exit()
						
			more_options()				
		


		if options == "exit":
			exit()
		if options == "cls":
			os.system("cls")
	
		
				
	Home()
