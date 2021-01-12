#Andrey Ilkiv 11/29/2020 Project Section 01 functions

#moved this part up here so i can use the isodd and iseven functions in my code earlier than the game
#Part 2 -------------------------------------------------

#Is even function
def is_even(value):
    if value%2 == 0:
        return True
##temp4 = is_even(6)
##print(temp4)
##print()


#Is odd function
def is_odd(value2):
    if value2%2 != 0:
        return True
##temp5 = is_odd(5)
##print(temp5)
##print()

#Is prime function
def is_prime(value3):
    if value3 <= 1:
        return False
    for i in range(2, value3):
        if value3 % i == 0:
            return False
    return True
##temp6 = is_prime(6)
##print(temp6)
##print()

#Is perfect function
def is_perfect(value4):
    total = 0
    for f in range(1, value4):
        if value4 % f == 0:
            total = total + f
    if total == value4:
        return True
    else:
        return False
##temp7 = is_perfect(6)
##print(temp7)
##print()
    
#Is abundant function
def is_abundent(value5):
    total2 = 0
    for g in range(1, value5):
        if value5 % g == 0:
            total2 = total2 + g
    if(total2 > value5):
        return True
    else:
        return False
##temp8 = is_abundent(12)
##print(temp8)
##print()

#part 1 -------------------------------------------------

#A -------------------------------------------------------

#Horizontal line function
def horizontal_line(width, char):
    pattern = ""
    for w in range(width):
        pattern = pattern + char
    return pattern
##print("Horizontal line, Width = 5:")
##temp = horizontal_line(5, "*")
##print(temp)
##print()

#Vertical line function
def vertical_line(shift, height, char2):
    pattern2 = ""
    for a in range(height):
        for b in range(shift):
            if shift != 0:
                if b >= 1:
                    if shift != 0:
                        pattern2 = pattern2 + " "
        pattern2 = pattern2 + char2 + '\n'
    return pattern2
##print("Vertical line, Shift=0 height=3:")
##temp2 = vertical_line(6, 3, "!")
##print(temp2)
##print()

#double verticle like || function
def double_vertical_line(shift, height, char2):
    pattern2 = ""
    for a in range(height):
        for b in range(shift):
            if shift != 0:
                if b >= 1:
                    if shift != 0:
                        pattern2 = pattern2 + " "
        pattern2 = pattern2 + char2 + char2 + '\n'
    return pattern2
##print("Vertical line, Shift=0 height=3:")
##temp2 = vertical_line(6, 3, "!")
##print(temp2)
##print()

#Two vertical lines function
def two_vertical_lines(width2, height2, char3):
    pattern3 = ""
    if width2 == 1:
        for c in range(height2):
            pattern3 = pattern3 + char3 + '\n'
        return pattern3
    else:
        for c in range(height2):
            pattern3 = pattern3 + char3
            for d in range(width2):
                if d > 1:
                    pattern3 = pattern3 + " "
            pattern3 = pattern3 + char3 + '\n'
        return pattern3
##print("Two Vertical Lines, width=3 height=3:")
##temp3 = two_vertical_lines(6, 3, "^")
##print(temp3)
##print()

#B -------------------------------------------------------

def number_1(width, char):
    if width != 0:
        pattern = vertical_line(width, 5, char)
        return pattern
    else:
        return ""
##print(number_1(2, "*"))

def number_0(width, char):
    if width != 0:
        if width != 1:
            pattern = horizontal_line(width, char) + '\n' + two_vertical_lines(width+2, 3, char) + horizontal_line(width, char)
            return pattern
        else:
            pattern = vertical_line(width, 5, char)
            return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_1(q, "*"))
##    print('\n' + '\n')

def number_2(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + vertical_line(width+2, 1, char) + horizontal_line(width, char) + '\n' + vertical_line(0, 1, char) + horizontal_line(width, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_2(q, "*"))
##    print('\n' + '\n')

def number_3(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + vertical_line(width+2, 1, char) + horizontal_line(width, char) + '\n' + vertical_line(width+2, 1, char) + horizontal_line(width, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_3(q, "*"))
##    print('\n' + '\n')

def number_4(width, char):
    if width != 0:
        pattern = two_vertical_lines(width+2, 2, char) + horizontal_line(width, char) + '\n' + vertical_line(width+2, 2, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_4(q, "*"))
##    print('\n' + '\n')

def number_5(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + vertical_line(0, 1, char) + horizontal_line(width, char) + '\n' + vertical_line(width+2, 1, char) + horizontal_line(width, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_5(q, "*"))
##    print('\n' + '\n')

def number_6(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + vertical_line(0, 1, char) + horizontal_line(width, char) + '\n' + two_vertical_lines(width+2, 1, char) + horizontal_line(width, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_6(q, "*"))
##    print('\n' + '\n')

def number_7(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + vertical_line(width+2, 4, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_7(q, "*"))
##    print('\n' + '\n')

def number_8(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + two_vertical_lines(width+2, 1, char) + horizontal_line(width, char) + '\n' + two_vertical_lines(width+2, 1, char) + horizontal_line(width, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_8(q, "*"))
##    print('\n' + '\n')

def number_9(width, char):
    if width != 0:
        pattern = horizontal_line(width, char) + '\n' + two_vertical_lines(width+2, 1, char) + horizontal_line(width, char) + '\n' + vertical_line(width+2, 2, char)
        return pattern
    else:
        return ""
##for q in range(0,11):
##    print(number_9(q, "*"))
##    print('\n' + '\n')

#C -------------------------------------------------------

def print_number(number, width, char):
    if number == 0:
        return print(number_0(width, char) + '\n')
    if number == 1:
        return print(number_1(width, char) + '\n')
    if number == 2:
        return print(number_2(width, char) + '\n')
    if number == 3:
        return print(number_3(width, char) + '\n')
    if number == 4:
        return print(number_4(width, char) + '\n')
    if number == 5:
        return print(number_5(width, char) + '\n')
    if number == 6:
        return print(number_6(width, char) + '\n')
    if number == 7:
        return print(number_7(width, char) + '\n')
    if number == 8:
        return print(number_8(width, char) + '\n')
    if number == 9:
        return print(number_9(width, char))

#Testing................

##print_number(0, 5, '*')
##print_number(1, 6, '*')
##print_number(2, 7, '*')
##print_number(3, 8, '*')
##print_number(4, 9, '*')
##print_number(5, 10, '*')
##print_number(6, 11, '*')
##print_number(7, 12, '*')
##print_number(8, 13, '*')
##print_number(9, 14, '*')

#D -------------------------------------------------------

def plus(width, char):
    width2 = int(format(width/2, '.0f'))
    if width != 0:
        if is_even(width) and width >3:
            pattern = double_vertical_line(width2, 2, char) + horizontal_line(width, char) + '\n' + double_vertical_line(width2, 2, char)
            return pattern
        else:
            pattern = vertical_line(width2+2, 2, char) + horizontal_line(width, char) + '\n' + vertical_line(width2+2, 2, char)
            return pattern
    else:
        return ""
##temp = plus(10, "*")
##print(temp)
##print()

def minus(width, char):
    if width != 0:
        pattern = '\n' + horizontal_line(width, char)
        return pattern
    else:
        return ""
##temp = minus(10, "*")
##print(temp)
##print()

#H -------------------------------------------------------

def multiply(width, char):
    center = int(format(width/2, '.0f'))
    if width != 0:
        pattern = two_vertical_lines(width, 1, char) + " " + two_vertical_lines(width-2, 1, char) + vertical_line(center+1, 1, char) + " " + two_vertical_lines(width-2, 1, char) + two_vertical_lines(width, 1, char)
        return pattern
    else:
        return ""
##temp = multiply(5, "*")
##print(temp)
##print()

#I -------------------------------------------------------

def division(width, char):
    center = int(format(width/2, '.0f'))
    if width != 0:
        pattern = vertical_line(center+2, 1, char) + '\n' + horizontal_line(width, char) + '\n' + '\n' + vertical_line(center+2, 1, char)
        return pattern
    else:
        return ""
##temp = division(5, "*")
##print(temp)
##print()

#E -------------------------------------------------------

def check_answer(number1, number2, answer, op):
    if op == "+":
        total = number1 + number2
        if total == answer:
            return True
        else:
            return False
    if op == "-":
        total2 = number1 - number2
        if total2 == answer:
            return True
        else:
            return False
    if op == "x":
        total3 = number1 * number2
        if total3 == answer:
            return True
        else:
            return False
    if op == "/":
        total4 = number1 / number2
        if total4 == answer:
            return True
        else:
            return False
        
##answer1 = check_answer(1, 2, 3, "+")
##print (answer1)
##answer2 = check_answer(1, 2, -1, "-")
##print (answer2)
##answer3 = check_answer(9, 5, 3, "+")
##print (answer3)
##answer4 = check_answer(8, 2, 4, "-")
##print (answer4)


def startask():
    startnum = int(input("Enter starting number (positive only): "))
    while startnum < 0:
        print("Invalid, try again")
        startnum = int(input("Enter starting number (positive only): "))
    return startnum

def endask():
    endnum = int(input("Enter ending number (positive only): "))
    while endnum < 0:
        print("Invalid, try again")
        endnum = int(input("Enter ending number (positive only): "))
    return endnum

def choice4check(value):
    if value < 10:
        string = str(value) + "                 "
    if value <100 and value > 9:
        string = str(value) + "               "
    if value > 99:
        string = str(value) + "            "
    if is_even(value) == True:
        string = string + "X"
    else:
        string = string + "               "
        
    if is_odd(value) == True:
        string = string + "X"
    else:
        string = string + "                          "
        
    if is_prime(value) == True:
        if is_odd(value) == True:
            string = string + "           "
        string = string + "X"
    else:
        string = string + "                "
        
    if is_perfect(value) == True:
        string = string + "X"
    else:
        string = string + "                  "
        
    if is_abundent(value) == True:
        string = string + "X"
        
    return string


    
