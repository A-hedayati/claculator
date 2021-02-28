print("In The Name Of ALLAH")
import math
print('''The Calculator.py
         Creation / edition date : 2/12/2021 
         Author : Chem Nobelium Admin
         Version 1.1
         features : Division, Multiplication, Sum, Sqrt (Others coming soon)''')
print("\_______________________________________/")
print('''
      1-Multiplication
      2-Division
      3-Sqrt
      4-Sum
      ''') # Please pay attention to this line of code (list of selection)
select = input(" Enter the number of calculator -> ")
if select == "1" or select == "Multiplication" or select == "multiplication":
    print(" Multiplication type")
    num_1 = float(input(" Enter the first number : "))
    num_2 = float(input(" Enter the second number: "))
    multi = num_1 * num_2
    print(f" {num_1} * {num_2} = {multi}")
    cycle = input("Do you want do this calculation again ? (yes/no):")
    if cycle == "yes" or cycle == "y" or cycle == "ye" or cycle == "Y" or cycle == "Ye" or cycle == "Yes": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
     print(" Multiplication type")
     num_1 = float(input(" Enter the first number : "))
     num_2 = float(input(" Enter the second number: "))
     multi = num_1 * num_2
     print(f" The {num_1} * {num_2} = {multi}")
    elif cycle == "no" or cycle == "No" or cycle == "NO" or cycle == "n" or cycle == "N" or cycle == "o" or cycle == "O" or cycle == "nO": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
        print("Thanks for calculate with my code")
        exit = input(" Press enter to exit ...  ")
elif select == "2" or select == "Division" or select == "division" :
     print(" Division type")
     num_1 = float(input(" Enter the first number : "))
     num_2 = float(input(" Enter the second number: "))
     div = num_1 / num_2
     print(f" {num_1} / {num_2} = {div}")
     cycle = input("Do you want do this calculation again ? (yes/no) : ")
     if cycle == "yes" or cycle == "y" or cycle == "ye" or cycle == "Y" or cycle == "Ye" or cycle == "Yes": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
         print(" Division type")
         num_1 = float(input(" Enter the first number : "))
         num_2 = float(input(" Enter the second number: "))
         div = num_1 / num_2
         print(f" {num_1} / {num_2} = {div}")
     elif cycle == "no" or cycle == "No" or cycle == "NO" or cycle == "n" or cycle == "N" or cycle == "o" or cycle == "O" or cycle == "nO": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
         print("Thanks for calculate with my code")
         exit = input(" Press enter to exit ...  ")
elif select == "sqrt" or select == "3" or select == "Sqrt":
    sqrtf = float(input(" Enter any number to calculate the sqrt : "))
    print(math.sqrt(sqrtf))
    cycle = input(" Do you want do this calculation again ? (yes/no) : ")
    if cycle == "yes"  or cycle == "y" or cycle == "ye" or cycle == "Y" or cycle == "Ye" or cycle == "Yes": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
     s = float(input(" Enter any number to recive the sqrt : "))
     print(math.sqrt(s))
     eixt = input("Press enter to exit ...")
    elif cycle == "no" or cycle == "No" or cycle == "NO" or cycle == "n" or cycle == "N" or cycle == "o" or cycle == "O" or cycle == "nO": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
        eixt = input("Press enter to exit ...") 
elif select == "sum" or select == "Sum" or select == "4":
    print(" Note : You can enter intiger and float number and negative and possitive number ")
    first_num  = float(input(" first number -> Enter any number to calculate the sum : "))
    second_num = float(input(" second number -> Enter any number to calculate the sum : "))
    result = first_num + second_num
    print(f" Result is equal to {first_num} + {second_num} = {result}.")
    cycle = input(" Do you want do this calculation again ? (yes/no) : ")
    if cycle == "yes" or cycle == "y" or cycle == "ye" or cycle == "Y" or cycle == "Ye" or cycle == "Yes": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax) 
     print(" Note : You can enter intiger and float number and negative and possitive number ")
     first_num  = float(input(" first number -> Enter any number to calculate the sum : "))
     second_num = float(input(" second number -> Enter any number to calculate the sum : "))
     result = first_num + second_num
     print(f" Result is equal to {first_num} + {second_num} = {result} .")
     eixt = input("Press enter to exit ... ")
    elif cycle == "no" or cycle == "No" or cycle == "NO" or cycle == "n" or cycle == "N" or cycle == "o" or cycle == "O" or cycle == "nO": # If user type wrong word the program won't give ERROR ! (please pay attention to the syntax)
        exit = input("Press Enter to exit ... ")
elif select != "1" or select != "Multiplication" or select != "multiplication" or select != "2" or select != "Division" or select != "division" or select != "3" or select != "Sqrt" or select != "sqrt" or select != "4" or select != "Sum" or select != "sum" : # if the User types wrong word the program won't be start (pay attention to the selection list)
    print(''' TYPE_ERROR : 
          The entered number or type is not valid.
          please try again''')
    exit = input(" Press enter to exit ... ")