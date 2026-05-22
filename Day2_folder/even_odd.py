#take user input and checking even or odd
number=int(input("enter the number : "))

if number%2==0 :                           # the % modulus gives the reminder 
    print(f"the number {number} is even")
else :
    print(f"the number {number} is odd")