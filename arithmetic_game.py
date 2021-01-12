#Andrey Ilkiv 11/29/2020 arithmetic game Section 01
import my_functions
import random

#G -----------------------------------------
correct = 0
wrong = 0
addition = 0
subtraction = 0
mult = 0
div = 0
addition_correct = 0
subtraction_correct = 0
mult_correct = 0
div_correct = 0
extraAattempts = 0
extraSattempts = 0
extraMattempts = 0
extraDattempts = 0
attempts = int(input("How many problems would you like to attempt? "))
while attempts < 0:
    print("Invalid number, try again", '\n')
    attempts = int(input("How many problems would you like to attempt? "))

wide = int(input("How wide do you want your digits to be? 5-10: "))
while wide < 5 or wide > 10:
    print("Invalid width, try again", '\n')
    wide = int(input("How wide do you want your digits to be? 5-10: "))
        
character = str(input("What character would you like to use? "))
while len(character) != 1 :
    print("String too long, try again")
    character = str(input("What character would you like to use? "))

drillmode = str(input("Would you like to activate drill mode? yes or no: "))
while drillmode != "yes" and drillmode != "no":
    print("Error, select either yes or no.")
    drillmode = str(input("Would you like to activate drill mode? yes or no: "))
print()
print("Here we go!")

if drillmode == "no":
    for i in range(attempts):
        print()
        print("What is .....", '\n')
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randsign = random.randint(0,3)
        if randsign == 0:
            sign = "+"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.plus(wide, character))
            my_functions.print_number(randnum2, wide, character)
            addition += 1
        if randsign == 1:
            sign = "-"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.minus(wide, character),'\n','\n')
            my_functions.print_number(randnum2, wide, character)
            subtraction += 1
        if randsign == 2:
            sign = "x"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.multiply(wide, character))
            my_functions.print_number(randnum2, wide, character)
            mult += 1
        if randsign == 3:
            sign = "/"
            while randnum2 == 0:
                    randnum2 = random.randint(0,9)
            while randnum1 % randnum2 != 0:
                randnum1 = random.randint(0,9)
                randnum2 = random.randint(0,9)
                while randnum2 == 0:
                    randnum2 = random.randint(0,9)
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.division(wide, character))
            my_functions.print_number(randnum2, wide, character)
            div += 1
        userIN = int(input("= "))
        if my_functions.check_answer(randnum1, randnum2, userIN, sign) == True:
            print("Correct!", '\n')
            correct += 1
        else:
            print("Sorry, that's not correct.")
    print("You got", correct, "out of", attempts, "correct!")
    
if drillmode == "yes":
    for i in range(attempts):
        print("What is .....", '\n')
        randnum1 = random.randint(0,9)
        randnum2 = random.randint(0,9)
        randsign = random.randint(0,3)
        if randsign == 0:
            sign = "+"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.plus(wide, character))
            my_functions.print_number(randnum2, wide, character)
            addition += 1
        if randsign == 1:
            sign = "-"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.minus(wide, character),'\n','\n')
            my_functions.print_number(randnum2, wide, character)
            subtraction += 1
        if randsign == 2:
            sign = "x"
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.multiply(wide, character))
            my_functions.print_number(randnum2, wide, character)
            mult += 1
        if randsign == 3:
            sign = "/"
            while randnum2 == 0:
                    randnum2 = random.randint(0,9)
            while randnum1 % randnum2 != 0:
                randnum1 = random.randint(0,9)
                randnum2 = random.randint(0,9)
                while randnum2 == 0:
                    randnum2 = random.randint(0,9)
            my_functions.print_number(randnum1, wide, character)
            print(my_functions.division(wide, character))
            my_functions.print_number(randnum2, wide, character)
            div += 1
            
        userIN = int(input("= "))

        if my_functions.check_answer(randnum1, randnum2, userIN, sign) == True:
            print("Correct!", '\n')
            if randsign == 0:
                addition_correct += 1
            if randsign == 1:
                subtraction_correct += 1
            if randsign == 2:
                mult_correct += 1
            if randsign == 3:
                div_correct += 1
                
        while my_functions.check_answer(randnum1, randnum2, userIN, sign) == False:
            print("Sorry, that's not correct.")
            userIN = int(input("= "))
            if randsign == 0:
                extraAattempts += 1
            if randsign == 1:
                extraSattempts += 1
            if randsign == 2:
                extraMattempts += 1
            if randsign == 3:
                extraDattempts += 1
            if my_functions.check_answer(randnum1, randnum2, userIN, sign) == True:
                print("Correct!", '\n')        

print("Thanks for playing!")
if drillmode == "yes":
    if addition > 0:
        print("Total addition problems presented", addition)
        print("Correct addition problems: ", addition_correct, " (", format((addition_correct/addition)*100, '.1f'), "%)", sep="")
        if extraAattempts == 0:
            print("# of extra attempts needed:", extraAattempts, " (perfect!)")
        else:
            print("# of extra attempts needed:", extraAattempts)
    else:
        print("No addition problems presented")
    print()

    if subtraction > 0:
        print("Total subtraction problems presented", subtraction)
        print("Correct subtraction problems: ", subtraction_correct, " (", format((subtraction_correct/subtraction)*100, '.1f'), "%)", sep="")
        if extraSattempts == 0:
            print("# of extra attempts needed:", extraSattempts, " (perfect!)")
        else:
            print("# of extra attempts needed:", extraSattempts)
    else:
        print("No subtraction problems presented")
    print()

    if mult > 0:
        print("Total multiplication problems presented", mult)
        print("Correct multiplication problems: ", mult_correct, " (", format((mult_correct/mult)*100, '.1f'), "%)", sep="")
        if extraMattempts == 0:
            print("# of extra attempts needed:", extraMattempts, " (perfect!)")
        else:
            print("# of extra attempts needed:", extraMattempts)
    else:
        print("No multiplication problems presented")
    print()

    if div > 0:
        print("Total division problems presented", div)
        print("Correct division problems: ", div_correct, " (", format((div_correct/div)*100, '.1f'), "%)", sep="")
        if extraDattempts == 0:
            print("# of extra attempts needed:", extraDattempts, " (perfect!)")
        else:
            print("# of extra attempts needed:", extraDattempts)
    else:
        print("No division problem presented")
