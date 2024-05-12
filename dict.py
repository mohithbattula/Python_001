#creating a dictionary
dictionary={}
print("This is a empty dictionary.")
#a dictionary exists in key value pairs
dictionary={'name':'Mohith','age':19,'city':'Vizag'}
print("The dictionary contains the elements:",dictionary)

#adding elements into a dictionary
dictionary['gender']='Male'
print("The dictionary contains the elements:",dictionary)

#removing of the element from the dictionary
del dictionary['age']
print("The dictionary contains the elements:",dictionary)

#changing the values of certain key
dictionary['city']='Bangalore'
print("The dictionary contains the elements:",dictionary)