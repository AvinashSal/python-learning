#making string utility tool
text=input("enter a string : ")

print("choice an opiton :")
print("1.Uppercase")
print("2.Reverse string")
print("3.Lowercase")
print("4.Vowel count")
print("5.palindrome check")
#taking user choice perform selected task
choice=int(input("enter a choice : "))

if choice==1 :
    print(text.upper())
    
elif choice==2 :
    print(text[::-1])  # text[start:stop:step] -1 is start from last character

elif choice==3 :
    print(text.lower())

elif choice==4 :
    vowel="aeiouAEIOU"
    count=0
    for char in text :
        if char in vowel:
            count+=1
    
    print("vowel count : ",count)

elif choice==5 :
    reverse=text[::-1]
    if text==reverse :
        print("string is palindrome ")
    else :
        print("string is not palindrome ")
        
else :
    print("Invalid choice")