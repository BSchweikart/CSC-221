"""
CSC 221
M1T1
Brian Schweikart
1/16/19
Goal: Gold
"""
import math

def main():
    """
    This program will calculate the largest 
    fishing pole that can fit diagonally in a box.
    """ 
    
    poleL = int(input("What is the length of your fishing pole? "))
    a = int(input("What is the length of the box? "))
    b = int(input("What is the width of the box? "))
    
    """
    ^ = counts as sq
    C^2 = A^2 + B^2
    A = length, B = width 
    """
    #A = length
    #B = width
    c = math.sqrt((a*a) + (b*b)) 
    
    print("The box can hold a fishing pole up to",c,"in length")
    if c >= poleL:
        print("The poll will fit")
    else:    
        print("The Fishing pole will not fit")
    
main()