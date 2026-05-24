#Using list and perform operations on list 

animals=["cat","dog","deer","lion"]        #this is animals list

print(animals)                             #printing for user to see it

print("operation can perform on list : ")
print("1.Add an animal ")
print("2.Remove an animal ")
print("3.Sort an animal list ")
print("4.Reverse an animal list")
print("5.")

choice=int(input("enter your choice : "))   #taking choice from user

if choice==1 :
    add_anim=input("enter an animal to add : ")
    print(animals)
    position=int(input("enter the position to add :"))     #user enter the position
    animals.insert(position-1,add_anim)                   #not an index position so {position-1}
    print(animals)





