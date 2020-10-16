#!/usr/bin/env python3


"""
Created on Wed Oct 14 19:59:04 2020

@author: Sourick
"""


import sys,os
import math


#find Prime number
def prime(n):
    flag = 1
    for i in range(2,(n//2) + 1):
        if n % 2 == 0:
            flag = 0
            break

    if flag == 1:
        return 1
    else:
        return 0

#find even number
def div2(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

#find lcm of a number
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

#Documentation
def documentation():
    print("(pow <space> value1 <space> value2): \n This is used to find power. \n")
    print("(fact <space> value): \n This is used to find factorial. \n")
    print("(sqrt <space> value): \n This is used to find root. \n")
    print("(gcd <space> value1 <space> value2): \n This is used to find gcd between 2 number. \n")
    print("(lcm <space> value1 <space> value2): \n This is used to find lcm between 2 number. \n")
    print("(floor <space> value): \n This is used to find floor value from a float number. \n")
    print("(ceil <space> value): \n This is used to find ceil value from a float number. \n")
    print("(sin <space> value): \n This is used to find sin value. \n")
    print("(cos <space> value): \n This is used to find cos value. \n")
    print("(tan <space> value): \n This is used to find tan value. \n")
    print("(prime <space> value): \n  Check whether given value prime or not [1 -> Prime, 0 -> Not Prime] \n")
    print("(div2 <space> value): \n Check whether given value even or odd [1 -> Even, 0 -> Odd] \n")
    print("(about <space> value): \n Display about this tool. \n")


#input taking process

in_data = input("")
command = in_data.split(" ")
data_list = list(in_data)


try:    

    #Dealing with buildin functions

    if (command [1] == "/"):

        data_list = list(in_data)
        data_list.pop()
        in_data = str(command[0])
        print(eval(in_data))

    elif (command[0] == 'pow'):
        print(int(math.pow(int(command[1]),int(command[2]))))

    elif (command[0] == 'sqrt'):
        print(math.sqrt(int(command[1])))
        
    elif (command [0] == 'fact'):
        print(int(math.factorial(int(command[1]))))
        
    elif(command [0] == 'gcd'):
        print(int(math.gcd(int(command[1]),int(command[2]))))
             
    elif(command [0] == 'lcm'):
        print(int(lcm(int(command[1]),int(command[2]))))

    elif(command [0] == 'floor'):
        print(math.floor(float(command[1])))
    
    elif(command [0] == 'ceil'):
        print(math.ceil(float(command[1])))
                
    elif(command [0] == 'sin'):
        print(math.sin(float(command[1])))
                
    elif(command [0] == 'cos'):
        print(math.cos(float(command[1])))
            
    elif(command [0] == 'tan'):
        print(math.tan(float(command[1])))
    
    elif(command[0] == 'prime'):
        print(prime(int(command[1])))

    elif(command[0] == 'div2'):
        print(div2(int(command[1])))
    
    elif(command[0] == 'about'):
        os.system("clear")
        print(" lipy Calculating Tool\n Version: 1.0.4 \n Developed By: Soujatya Bhattacharya")

    elif(command[0] == 'help'):
        os.system("clear")
        documentation()

except ArithmeticError:
    print("Division has failed!!")

except:
    print("Invalid Parameters!!")


  

