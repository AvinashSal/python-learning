#making string utility tool
text=input("enter a string : ")

#taking user choice perform selected task
choice=int(input("enter a choice : "))

if choice==1 :
    print(text.upper())
    
elif choice==2 :
    print(text[::-1])  # text[start:stop:step] -1 is start from last character

elif choice==3 :
    print(text.lower())