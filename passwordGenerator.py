# -*- coding: utf-8 -*-
from __future__ import print_function
import random

#creates and returns single password
def generateSinglePassword():
    possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789)!@#$%^&*("
    passw = "" #empty password for now, will add characters, number and symbols to it below
    
    #choose 4 alpha characters to add to password
    for a in range(4):
        choice = random.randint(0,51)
        passw += possibleCharacters[choice]
    
    #choose 2 numbers to add to password
    for a in range(2):
        choice = random.randint(52,61)
        passw += possibleCharacters[choice]
    
    #choose two characters to add to password
    for a in range(2):
        choice = random.randint(0,51)
        passw += possibleCharacters[choice]
    
    #choose two symbols to add to password
    for a in range(2):
        choice = random.randint(62,71)
        passw += possibleCharacters[choice]
    
    return passw;

#makes num calls to the function generateSinglePassword to create num passwords
#and returns a list of num passwords
def generatePassword(num):
    passwords = ""
    for a in range(num):
       passwords += generateSinglePassword() + "\n"
    return passwords 

#print starting title for program
print ("PASSWORD GENERATOR 1.0")
print ("------------------------------------------------------")
print ("All generated passwords have the following format:")
print ("   * First 4 characters are alpha (Upper and Lower)")
print ("   * Next  2 characters are digits (0-9)")
print ("   * Next  2 characters are alpha (Upper and Lower)")
print ("   * Last  2 characters are symbols")
print()

#prompt the user for how many passwords they want to generate,
#and then make a call to function generatePassword(n) to get
#a list of that many passwords
num = raw_input("How many password do you want to generate: ")
print (generatePassword(int(num)))
print()

#sentinel controlled loop to continually run the creation of passwords
#as long as the user responds (y)
response = raw_input("Want to run again (y): ")
while(response == "y"):
    num = raw_input("How many password do you want to generate: ")
    print (generatePassword(int(num)))
    print()
    response = raw_input("Want to run again (y): ")

#Program is over
print ("Thanks for using the Password Generator 1.0!!!")
