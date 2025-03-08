# making an incresing triangle 
""" 
n = 5

*
**
***
****
*****

"""
n = int(input("Enter the size of the triangle : "))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()

# making an decreasing triangle 
""" 
n = 5

*****
****
***
**
*

"""
n = int(input("Enter the height of the reversed triangle : "))
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end='')
    print()
    

#Square pattern 
""" 
n = 5

*****
*****
*****
*****
*****

"""
n = int(input("Enter the height of the square : "))
for i in range(n+1):
    for j in range (n+1):
        print("*",end='')
    print()

# making an right sided incresing triangle - inverted space triangle + increasing star triangle
""" 
n = 5

    *
   **
  ***
 ****
*****

"""
n = int(input("Enter the height of the right sided incresing triangle : "))
for i in range(n+1):
    for j in range(n,i,-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()

# making an right sided decreasing triangle - increasing space triangle + decreasing star triangle
""" 
n = 5

*****
 ****
  ***
   **
    *
    
"""
n = int(input("Enter the height of the right sided decresing triangle : "))
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    print()

#Hill pattern - decreasing space triangle + right sided increasing triangle + increasing triangle
""" 
n = 5

     *
    ***
   *****
  *******
 *********

"""
n = int(input("Enter the height of the hill : "))
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    for j in range(i):
        print("*",end='')
    print()

    
# Reverese Hill pattern - increasing space triangle + right sided decreasing triangle + deccreasing triangle
""" 
n = 5

*******
 *****
  ***
   *
   
""" 
n = int(input("Enter the height of the hill : "))
for i in range (n):
    for j in range(i):
        print(" ",end='')
    for j in range(n,i,-1):
        print("*",end='')
    for j in range(n-1,i,-1):
        print("*",end='')
    print()
        
#Diamond pattern upper hill + lower hill
""" 
n = 5

     *
    ***
   *****
  *******
  *******
   *****
    ***
     *

"""
n = int(input("Enter the height of the diamond : "))
for i in range(n-1):
    for j in range(n-1,i,-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    for j in range(i):
        print("*",end='')
    print()
for i in range (n):
    for j in range(i):
        print(" ",end='')
    for j in range(n,i,-1):
        print("*",end='')
    for j in range(n-1,i,-1):
        print("*",end='')
    print()