#Mutlifunction tool
print("Hello There")
print("Could you please enter your firstname")
firstname = input()
print("Now can you please enter your surname")
surname = input()
print("Welcome,",firstname,surname)
print("Before we get started, can you confirm that this is name")
fullname = firstname+" "+surname
print(fullname)
correct = input()

if correct == "yes" or correct == "Yes":
      username = surname[0]+""+surname[1]+""+surname[2]+""+firstname[0]+""+str(len(surname))
      print("Your username is:",username)
      print("Please enter a password")
      password = input()
      print("Please re-enter your pasword")
      password1 = input()
      if password1 == password:
            print("Thank you")
            print("What system do you what to use")
            print("The systems that are Calculator or Sleep Calculator or Guessing Game")
            system = input()
            print(system)
            if system == "calculator" or system == "Calculator":
               print("Welcome to the calculator")
               print("Please can login")
               print("Username")
               user1 = input()
               print("password")
               pass1 = input()
               if user1 == username and pass1 == password:
                   print("Access Granted")
                   print("Please enter your two numbers - one at a time")
                   number = int(input())
                   number1 = int(input())
                   print("please enter what you would like to do with these numbers")
                   function = input()
                   if function == "add":
                         answer = number + number1
                         print(answer)
                   if function == "subtract":
                         answer = number - number1
                         print(answer)
                   if function == "divide":
                         answer = number / number1
                         print(answer)
                   if function == "mutliple":
                         answer = number * number1
                         print(answer)
                         input("\nPress ENTER to exit program")
            if system == "sleep calculator" or system == "Sleep Calculator":
                  print("Welcome to the Sleep Calculator")
                  print("Please can login")
                  print("Username")
                  user1 = input()
                  print("password")
                  pass1 = input()
                  if user1 == username and pass1 == password:
                        print("Access Granted")
                        hourspernight = input("How many hours per night do you sleep? ")
                        hoursperweek = int(hourspernight) * 7
                        print ("You sleep",hoursperweek,"hours per week")
                        hourspermonth = float(hoursperweek) * 4.35
                        print ("You sleep",hourspermonth,"hours per month")
                        dayspermonth = float(hourspermonth) / 24
                        print ("This equates to",dayspermonth,"days per month")
                        hoursperyear = float(hourspermonth) * 52
                        print ("You sleep",hoursperyear,"hours per year")
                        input ("\nPress ENTER to exit program")
            if system == "guessing game" or system == "Guessing Game":
                  print("Welcome to the guessing game")
                  print("Please can login")
                  print("Username")
                  user1 = input()
                  print("password")
                  pass1 = input()
                  if user1 == username and pass1 == password:
                        print("Access Granted")
                        import random
                        rnumber = random.randint(1,100)
                        unumber = int(input("Enter a number "))
                        attempts = 0
                        while unumber != rnumber:
                              if unumber < rnumber:
                                    print("You have guessed to low")
                                    unumber = int(input("try again "))
                                    attempts = attempts + 1
                              elif unumber >rnumber:
                                          print("You have guessed to high")
                                          unumber = int(input("try again "))
                                          attempts = attempts + 1
                        print("You Win! You had",attempts,"at guessing.")
                        input ("\nPress ENTER to exit program")