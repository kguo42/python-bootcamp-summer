# May 14th
# Kay Guo and Oscar A. Chavez Ortiz
# Example script walk you through


'''
This example script will walk you through what a python script is 
and does and what the Python interpretor will do when it runs a script.
The main thing to keep in mind is that computers are really good 
when you outline EXPLICITLY everything you want them to do. 
This is because when you run a script most programming languages 
read the script from top to bottom. Executing the lines of code as they
pass them. This means that the order of how you declare variables and define functions 
is crucial to the execution of your code/script. 
Let us look at some basics of coding in the python language 
while also going over what is going on under the hood when you run a python script.
'''





# Some example code that imports packages (we will cover this in a later session)
import math
import numpy as np

#######################################
#You may have noticed that there are lots of #'s and 
#the reason for that is to document or "Comment" your code
#Everything after the # will be ignored by python when you run this script 
#Commenting your code is also a good way for you and others to know what your code is doing 
#######################################



#The coding 101 exercise is to simply display a message to the command line prompt
#We call a built in Python function called print and we provide it with some text we want to display
# Note: The text to be displayed NEEDS to be in quotation marks otherwise you will get an error
print('Hello World')


#This is how we assign a value to a variable 
#We use the assignment operator(the = sign) to assign a value to a variable
#In this example we are assigning the value of 1 to 'a'
#This value will be stored in memory so anywhere else in the code that you call 'a', 
#Python will know that 'a' is assigned to 1
a = 1 

###############################
# NOTE: even though we do not explicitly see the a = 1 on the screen it is being assigned "under the hood"
# The only time that we can see the result of an operation is when we display it onto the screen via print or through printing other
# Verification steps, we will cover these in more detail later in the debugging session
###############################

#Here we are making a display prompt that outputs the value of 'a' onto the screen
print('The value of a is ', a)

#One cool thing in coding that we can do is assign variable to operations of other variables. 
#Let me explain what I mean with the following example
#In a couple of lines above we have assigned the value of 1 to 'a' but let us say we wanted to
#make another value that changes 'a' and we wanted to store that
#value into another variable. So let us take 'a' and add 1 to it and store that onto another variable 'b'
b = a + 1

#################
#Note: under the hood b is being assigned the value of a + 1 = 1 + 1 = 2 
#################

#######
#We display the value of b with the code below
#######
print('The value of b is ', b)

###############
#With the following code we will show an example of being cautious with variable names and declarations
#In some cases you will be asked to perform an operation on a variable, 
#this could be because you need to compute the mass of a star
#Or some other astrophysical measurement. 
#Let us take an example where we take 'b' and multiply it by 2 but instead of storing it to another 
#variable we assign it the variable 'b'.
###############
b = b * 2

#############
#What Python will do for the above line of code is to update the value of 'b' in memory
#Prior to this 'b' was 2 and so it will carry out the operation of b*2 = 2*2 = 4 and then what will
#occur is that this value of 4 will be assigned to 'b' 
#which will overwrite the previous value of 'b' which was 2
#so now 'b' will be 4
#############

print('The value of b is ', b)


################
# Order of operations in python script. 
################
# As we mentioned on the top lines, python scripts are read top down and then executed sequentially
# This means that variable and functions get stored in memory whenever they come up, as they come up
# Below is an example of this in action. 
# We are trying to use a function called print_value but we can see that the function declaration
# Fancy word for saying where we define the function, is after the function call
# What python will try to do is try to execute the function print_value but because we have not 
# Defined the function prior to using it Python cannot find a reference to it in memory 
# So we need to change the order of how this script is executed so that print_value is defined
# and stored in memory first, then once it is stored in memory we can call the function and execute the 
# function as normal.
################


#could you pls try to fix the error?
print_value(a)

def print_value(a):
    
    """ print the value of the input argument"""
    
    print(f'The input argument is: {a}')
    
    
    