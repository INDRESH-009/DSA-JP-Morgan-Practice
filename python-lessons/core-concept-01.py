#core concepts for solving interview questions in python from neetcode video titled : "Python for Coding Interviews - Everything you need to Know"

""" 
INDEX : 
1.Variables
2.If statement 
3.Loops 
4.Math
"""
#-----------------------------------------------------------------------
# 1. VARIABLES

#dynamically typed and the type is decided at runtime so types of variable can change in the course of the program
n=0
print(n)
n="abc"
print(n)

#multiple assignments of same or different types can be made in the same line
n,m = 0,"abc"
l1,l2 = {},{}

#incrementing and decrementing - n++ and n-- doesnt work
n=n+1
n+=1

#Absense of value in python is called None like null in JS , it can aslo be assigned to variables 
a = 10
a = None
print(a)

#-----------------------------------------------------------------------
# 2. IF STATEMENTS
n=1
if n>2:
    print("Hello")
elif n<2:
    print("World")
else:
    print("What?")

# for single line conditions like above parenthesis is not required by python but required for multiline conditions 
#Logical operators like && and || are represented as "and" , "or" respectively
if((n>2 and n!=m) or n==m):
    print("wow")
    
#-----------------------------------------------------------------------
# 3. LOOPS 

#while loops : initialise the iterator , loop and then increment 
n=5
while n>0:
    print(n)
    n = n-1 

#for loops : 2 ways of looping 
#method 01 - loop using a iterator 
l = [10,20,30,40,50]
for i in range(len(l)):
    print(l[i])

#range working - range(start,end,step) - start inclusive , end not inclusive
for i in range(0,len(l),2):
    print(l[i])
    
#print from 2 to 5
for i in range(2,6):
    print(i)
    
#print from 5 to 2 
for i in range(5,1,-1):
    print(i)

#method 02 - loop directly over the elements without iterator 
for nums in l:
    print(nums)

#-----------------------------------------------------------------------
# 4. MATHEMATICS

#division is decimal by default
print(5/2)

#for integer division use // which rounds the number 
print(5//2)

#for negative numbers most language round towards 0 by default , but in python negative numbers are rounded downwards - (-1.5)=>(-2) in py but generally (-1.5)=>(-1)
print(-3//2)    

# A workaround for rounding towards 0 for -ve numbes is to use decimal division and then convert it into int 
print(int(-3/2))

#modding is similar to most language
print(10%3)
#Except for negative numebrs
print(-10%3)
#So to be consistent with modulo of other languages
import math
print(math.fmod(-10,3))

#floor method explicitly rounds down
print(math.floor(3/2))
#ceil method explicitly rounds up
print(math.ceil(3/2))
#use math.sqrt for finding roots
print(math.sqrt(2))
#use math.pow for finding powers
print(math.pow(2,3))

#If you want max or min int use 
float("inf")
float("-inf")
#lets check it against a large number 
print(math.pow(2,200)<float("inf"))
