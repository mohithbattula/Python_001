#creating a list 
list=[]
print("This list contains no elements.")
#creating a list with elements inside it 
list1 = [1,2,3,4,5]
print(list1)

#adding elements to the list 
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.append(10)
print(list)

#adding elements in the list by taking user inputs
list_new=[]
print("Enter the number of elements you need in the list:")
n=int(input())
for i in range(n):
    list_new.append(int(input()))
print(list_new)

#removing of an element from the list
list_new.remove(2)
print(list_new)

#updating an element from the list
list_new[1]=10
print(list_new)