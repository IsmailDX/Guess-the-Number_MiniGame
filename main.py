import random
print("********RULES********\n"
      "- If the number the user inputted is equal to the original number than the user wins\n"
      "- If the number the user inputted is less than or greater than the original number,\n then "
      "the user will get a total of 10 attempts to guess the number\n"
      "- If the user ran out of attempts then he/she lost\n")

origin_num = random.randint(0,100) #original number

i = 1
Trys = 10  # Total number of attempts
while i <= 10:

    user_in = int(input("* Guess a number: "))  # taking user input

    if user_in < origin_num:  # if user input is less than the original number
        i += 1
        Trys -= 1
        print("* Your number:", user_in, "is smaller than the original number\n* Number of attempts left:", Trys, "\n")

    elif user_in == origin_num:  # if user input is equal to the original number
        print("\n********YOU WON!!!********\nYour number:", user_in, "is equal to the original number:", origin_num,
              "\n")
        break

    else:  # if user input is greater than the original number
        i += 1
        Trys -= 1
        print("* Your number: ", user_in, " is greater than the original number\n* Number of attempts left:", Trys,
              "\n")

if i >= 11:
    print("* You ran out of Attempts * \nYou lost the original number is:", origin_num)
