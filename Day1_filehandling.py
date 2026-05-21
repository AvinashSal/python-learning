#basic open file and read
f = open("file_handlingeasy.txt","r")
print(f.read())               # read the file
f.close()

#basic open the file "with" by this no need to close the file
with open("file_handlingeasy.txt","a") as f:
    f.write("file is appended with this sentence")
    
with open("file_handlingeasy.txt") as f:
    print(f.read())                       #to check the appended sentence in the file
    
#file is writen by another sentence and all first is deleted
with open("file_handlingeasy.txt","w") as f:
    f.write("oops file is modified or rewriten")

with open("file_handlingeasy.txt") as f:
    print(f.read())
    
#creating new file
f=open("file_handlingeasy2.txt","x")
with open("file_handlingeasy2.txt","w") as f:
    f.write("new file is created")
with open("file_handlingeasy2.txt") as f:
    print(f.read())
#deleting or removing the file 
# {{{{ import os
#      os.remove("file_handlingeasy2.txt") }}}
