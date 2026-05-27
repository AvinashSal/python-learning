#learning list methods 

#list is below perform the list methods on it
nums=[62,45,18,10,16,19,20,17]

#lets sort the list
nums.sort()
print(nums)

#lets remove the specified position like index element remove
nums.pop(1)
print(nums)

#lets remove the specified value in list
nums.remove(10)   
print(nums)

#lets add the new element 
nums.append(55)
print(nums)

#lets find length of list
# nums.
# print(nums)

#make a copy of list
# nums1=nums.copy()
print(nums.copy())

#count the string,number etc in list
print(nums.count(20))

#extend the list by any iterable list,set,tuple etc
tup1=(1,2,3,4)
nums.extend(tup1)
print(nums)

list1=["hi","extend"]
nums.extend(list1)
print(nums)

#index of list elements 
print(nums.index(20))


#add{insert(position,element)} an element in any position in given list ,append add only at end
nums.insert(3,"inserted")
print(nums)

#reverse the list 
nums.reverse()
print(nums)

#sort reverse the list 
odd=[5,3,7,1,13,21,11]
odd.sort(reverse=True)
print(odd)

#function as length of string to sort it as reverse
def Myfun(name):
    return len(name)

names=['avinash','shubham','chetan','gana','tukaram','sonya']
names.sort(reverse=False,key=Myfun)
print(names)

#remove all element or clear the list
nums.clear()
print(nums)

