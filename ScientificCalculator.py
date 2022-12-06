import math

# Number Calculator
def calculation(num1, sign, num2): 
    if sign == "+":
        result = int(num1) + int(num2)
        print("Answer is: ", result)
    elif sign == "-":
        result = int(num1) - int(num2)
        print("Answer is: ", result)
    elif sign == "x":
        result = int(num1) * int(num2)
        print("Answer is: ", result)
    elif sign == "/":
        result = int(num1) / int(num2)
        print("Answer is: ", result)
    elif sign == "%":
        result = int(num1) % int(num2)
        print("Answer is: ", result)
    else:
        print("Invalid Input Data")
    print("_________________________________________________________________________________")

# Trigonometric Calculator
def calculation2(func, angle):
    if func == "sin":
        value = math.sin(angle)
        print("Answer is: ", value)

    elif func == "cos":
        value = math.cos(angle)
        print("Answer is: ", value)

    elif func == "tan":
        value = math.tan(angle)
        print("Answer is: ", value)

    elif func == "cosec":
        value = 1 / math.sin(angle)
        print("Answer is: ", value)

    elif func == "sec":
        value = 1 / math.cos(angle)
        print("Answer is: ", value)

    elif func == "cot":
        value = 1 / math.tan(angle)
        print("Answer is: ", value)

    else:
        print("Invalid Input Data")
    print("_________________________________________________________________________________")

def calculation3(a):
         if a == "S":
            ask = input("Number: ")
            ans = math.sqrt(int(ask))
            print("Answer is: ",ans)
         elif a == "E":
            ask = int(input("Number: "))
            power = int(input("Power: "))
            ans = int(ask) ** int(power)
            print("Answer is: ",ans)
         elif a == "DR":
            ask = input("Degrees: ")
            ans = math.radians(int(ask))
            print("Answer is: ",ans)
         elif a == "RD":
            ask = input("Radians: ")
            ans = math.degrees(int(ask))
            print("Answer is: ",ans)
         else:
            print("Invalid Input Data")
         print("_________________________________________________________________________________")
 


print("Welcome to the Calculator. --- 2022 (C)Aditya Chavan")
print("_________________________________________________________________________________")
print("This Calculator consists three Parts:")
print("(1) Number Calculator -- N")
print("(2) Trigonometric Calculator -- T")
print("(3) Advanced Calculator -- A")
print("(4) To exit from the Calculator -- Q")
print("________________________________________________________________________________")

while True:
     z = input("Select any one Task: (N/T/A/Q): ")
     if z == "N":
         print("Number Calculator")
         print("--------------------------------------------------------------------------------")
         print("General Instructions: You can use Sign as ('+', '-', 'x', '/', '%)")
         print("First number and Second number should be Integer")
         print("--------------------------------------------------------------------------------")

         a = input("First number: ")
         b = input("Sign: ")
         c = input("Second number: ")    
         calculation(a, b, c)
 
     elif z == "T":
         print("Trigonometric Calculator")
         print("--------------------------------------------------------------------------------")
         print("General Instructions: You can use Trigonometric Functions like (sin, cos, tan, sec, cosec, cot)")
         print("Angle should be Degrees. For Example- 15, 30, 45, 90, etc........")
         print("--------------------------------------------------------------------------------")

         func = input("Trigonometric Function: ")
         angle = int(input("Angle in Degrees: "))
         a = math.degrees(angle)
         calculation2(func, a)

     elif z == "A":
         print("Advanced Calculator")
         print("--------------------------------------------------------------------------------")
         print("General Instructions: These are the things you can do with the Advanced Calculator..... ")
         print("(1) To Find Square Root - S ")
         print("(2) To Find Exponent - E")
         print("(3) To Convert Angle Degree --> Radian - DR")
         print("(4) To Convert Angle Radian --> Degree - RD")
         print("--------------------------------------------------------------------------------")

         a = input("Select the Task: ")
         calculation3(a)
        
     elif z == "Q":
        break

     else:
        print("Invalid Input Data")
