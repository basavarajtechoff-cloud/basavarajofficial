my_list=[1,2,3,4,5,6]

new_list=[i*i for i in my_list]      # use of list comprehension wrtie code within list to create new list from existing list. here we are creating new list with square of elements in my_list

print(new_list)  # This will print the new list containing the squares of the elements in my_list.

new_list=[i*i for i in my_list if i%2==0]  # This will create a new list containing the squares of even numbers from my_list.
print(new_list)  # This will print the new list containing the squares of the even numbers in my_list.

new_list=[i*i for i in my_list if i%2==0 and i>3]  # This will create a new list containing the squares of even numbers greater than 3 from my_list.
print(new_list)  # This will print the new list containing the squares of the even numbers

#Dictionary

my_dict = {'a':1,'b':2,'c':3}  # Creates a dictionary with keys 'a', 'b', 'c' and corresponding values 1, 2, 3.
print(my_dict)  # Displays the entire dictionary.

my_dict['d']=4  # Adds a new key-value pair 'd':4 to the dictionary.
print(my_dict)  # Displays the updated dictionary.

my_dict['a']=10  # Updates the value associated with key 'a' to 10.
print(my_dict)  # Displays the dictionary after the update.

my_dict.pop('b')  # Removes the key-value pair with key 'b' from the dictionary.
print(my_dict)  # Displays the dictionary after removing the key 'b'.

print(my_dict.keys())  # Displays all the keys in the dictionary.
print(my_dict.values())  # Displays all the values in the dictionary.

print(my_dict.items())  # Displays all the key-value pairs in the dictionary as tuples.

my_dict2= {'a':1,'b':2,'c':3,'basav':{'b1':1,'b2':2,'a1':3}}  # Creates a nested dictionary with another dictionary as the value for key 'basav'.
print(my_dict2)  # Displays the entire nested dictionary.
print(my_dict2['basav']['b2'])  # Displays the value associated with key 'b2' in the nested dictionary under key 'basav'.

my_dict3= {'a':1,'b':2,'c':3,'basav':[1,2,3,4]}  # Creates a dictionary with a list as the value for key 'basav'.
print(my_dict3)  # Displays the entire dictionary with the list.    

print(my_dict3['basav'][2])  # Displays the third item in the list associated with key 'basav' in the dictionary.   
new_dict={i:i*i for i in range(1,6)}  # Creates a new dictionary where keys are numbers from 1 to 5 and values are their squares using dictionary comprehension.
print(new_dict)  # Displays the newly created dictionary with squares of numbers from 1 to 5.

#dictionary comprehension with condition
new_dict={i:i*i for i in range(1,6) if i%2==0}  # Creates a new dictionary with squares of even numbers from 1 to 5.
print(new_dict)  # Displays the newly created dictionary with squares of even numbers from 1 to 5.


x= [1,2,3]
y=x
y.append(4)  # Appends 4 to the list y, which is a reference to the same list as x.
print(x)  # Displays the list x, which now includes the appended value 4 since

#craeted new branch