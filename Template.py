"""
CTEC 121
<Garrett>
<Mod 2 Programming Assignment>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from math import *
import math

def main():
    
    #Assignment Statements
    print()
    exampleString = "Here is some example text."
    print(exampleString)
    print(type(exampleString))

    exampleInt = 8
    print()
    print(exampleInt)
    print(type(exampleInt))
    print()

    print("\n example formula")
    r = 5
    v = (4/5)*pi*r**2
    print("v:",v)

    #End and sep examples
    print()
    print("Here is some example text", end="_")
    print('1', '2', '3', sep="_")

    #Tab, quote, and backslash
    print()
    print("\t \"Example text\\!\"")
    
    
    #Input from user
    print()
    myString = input("Enter text: ")
    print(myString)
    print()
    myInt = int(input("Enter a number: ")) #Only numbers are accepted
    print(myInt)
    print()
    myFloat = float(input("Enter a decimal number: ")) #Only numbers with decimals should be accepted
    print(myFloat)
    print()
    myEval = eval(input("Enter an expression: ")) 
    print(myEval)
    
    #Simultaneous Assignment

    print()
    x, y = eval(input("Enter two numbers separated by a comma: "))
    print(x,y)
    print()
    x, y = input("Enter two numbers: ").split()
    print(x,y)
    
    
    #Integer Arithmetic
    print()
    x = 5/2
    print(x)
    print()
    y = 5%2
    print(y)
    

    #Definite Loops

    print()
    for i in [5, 3, 2]:
        print(i)
    print()
    for count in range(3):
        print(count)
    print()
    for i in range(11,26,3):
        print(i)
    

    #Demonstrating use of various functions, expressions, and values
    
    print("Here is pi!")
    print(math.pi)
    print()
    x = int(input("Enter a value for x to find the square root: "))
    print(math.sqrt(x))
    print()
    
    print("Here is pi rounded up!")
    print(math.ceil(math.pi))
    print()
    print("Here is pi rounded down!")
    print(math.floor(math.pi))
    

    #Square and Cube values

    print()
    x = int(input("Enter a value of x to square: "))
    print(x**2)
    print()
    y = int(input("Enter a value of y to cube: "))
    print(y**3)
    

    #Accumulator Pattern

    print()
    a, b, c, d = eval(input("Enter values for a, b, c, d, separated by commas: "))

    sum = 0
    for i in [a, b, c, d]:
        sum = sum + i
    print(sum)
    

    #Bonus!
    print()
    r = int(input("Enter a value for r to find the volume: "))
    V = (4/3)*pi*(r**3)
    print(V)
    
    print()
    r = int(input("Enter a value for r to calculate area: "))
    A = 4*pi*(r**2)
    print(A)
    
    print()
    x1, y1, x2, y2 = eval(input("Enter values for x1, y1, x2, and y2, separated by commas to calculate slope: "))
    m = ((y2-y1)/(x2-x1))
    print(m)
    
    print()
    a, b, c = eval(input("Enter values for a, b, and c, separated by commas to calculate s: "))
    s = (a+b+c)/2
    print(s)
    
    print()
    s, a, b, c = eval(input("Enter values for s, a, b, and c, separated by commas to calculate A: "))
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)
    print()
    print("End of assignment.")
main()    