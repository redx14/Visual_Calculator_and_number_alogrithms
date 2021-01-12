#Andrey Ilkiv numbers program 11/29/2020 section 01

import my_functions

selection = 0
startnum = 0
endnum = 0


while int(selection) != 5 :
    print("Main Menu", '\n')

    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Chart all even, odd, prime, and abundant numbers within a given range")
    print("5 - Quit")
    print()
    print()

    
    selection = str(input("Your choice: "))
    if selection == "5":
        print()
        print("Goodbye!")
    else:
        if selection == "1" or selection == "2" or selection == "3" or selection == "4":
            selection = int(selection)
        else:
            print("I don't understand that ...")
            selection = 0
            print()
            print()

    #start here for code
    
    if selection == 1:
        startnum =  my_functions.startask()
        endnum = my_functions.endask()
        while endnum < startnum:
            print("Invalid, Try again")
            endnum = my_functions.endask()
        print()
        print("All prime numbers between", startnum, " and", endnum)
        print("##############")
        for i in range(startnum, endnum+1):
            if my_functions.is_prime(i) == True:
                print(i)
        print("##############")
        print()
        
    if selection == 2:
        startnum =  my_functions.startask()
        endnum = my_functions.endask()
        while endnum < startnum:
            print("Invalid, Try again")
            endnum = my_functions.endask()
        print()
        print("All perfect numbers between", startnum, " and", endnum)
        print("##############")
        for j in range(startnum, endnum+1):
            if my_functions.is_perfect(j):
                print(j)
        print("##############")
        print()
        
    if selection == 3:
        startnum =  my_functions.startask()
        endnum = my_functions.endask()
        while endnum < startnum:
            print("Invalid, Try again")
            endnum = my_functions.endask()
        print()
        print("All perfect numbers between", startnum, " and", endnum)
        print("##############")
        for k in range(startnum, endnum+1):
            if my_functions.is_abundent(k):
                print(k)
        print("##############")
        print()
        
    if selection == 4:
        startnum =  my_functions.startask()
        endnum = my_functions.endask()
        while endnum < startnum:
            print("Invalid, Try again")
            endnum = my_functions.endask()
        print()
        print("Number      Even      Odd      Prime      Perfect      Abundent")
        for p in range(startnum, endnum+1):
            print(my_functions.choice4check(p))
