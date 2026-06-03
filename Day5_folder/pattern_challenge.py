"""

"""
n=5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
for i in range(1,n):
    for k in range(i+1):
        print(" ",end="")
    for j in range(n-i):
        print("* ",end="")
    print()
    
for i in range(1,n+1):
    space=" "*(n-i)
    star="* "*(i)
    print(space+star)
    
for i in range(1,n+1):
    space=" "*(i)
    star="* "*(n-i)
    print(space+star)
    
for i in range(1,n+1):
    if i==1 or i==n :    #if i in(1,n)
        print("* "*(n))
    else :
        for j in range(1,n+1):
            if j in (1,n) :     #if j in (1,n)
                print("* ",end="")
            else :
                print("  ",end="")
        print()
   
for i in range(1,n+1):
    if i==1 or i==n or i==2 :
        star="*"*i
        print(star)
    else :
        for j in range(1,i+1):
            if j==1 or j==i :
                print("*",end="")
            else :
                print(" ",end="")
        print()
    
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    if i==1 or i==n :
        for k in range(1,i+1):
            print("* ",end="")
    else :
        for m in range(1,i+1):
            if m==1 :
                print("*",end="")
            elif m==i :
                for j in range(i-1):
                    print(" ",end="")
                print("*",end="")
            else:
                print(" ",end="")
        
    print()