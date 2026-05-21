name =input("enter your name :")
print(f"your name is {name}")
age =input("enter your age :")      #input take default as string
print("you are "+age+" years old") #show output without error because it is string
age = int(input("enter your age :"))
print("you are "+age+" years old")   #it will show the error str + int
print("you age ",age,"years old")    #it will not give error now