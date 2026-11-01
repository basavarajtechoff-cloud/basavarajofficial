print ("Hello World")  # Displays a greeting in the console.

a=10  # Assigns the integer 10 to variable a.
b=20  # Assigns the integer 20 to variable b.

print('before swap')  # Labels the values before they are swapped.
print(a)  # Displays the current value of a.
print (b)  # Displays the current value of b.

#swap  # Marks the section where the two variables are swapped.
a,b=b,a  # Swaps the values of a and b using tuple unpacking.

print('after swap')  # Labels the values after they are swapped.
print(a)  # Displays the new value of a.
print(b)  # Displays the new value of b.


my_list = [1,2,"Basav","DN",['aa','bb','cc']]  # Creates a list containing numbers, strings, and a nested list.
print(my_list[0])  # Displays the first item in the list.
print(my_list[4][1])  # Displays the second item in the nested list.
print(my_list[0:2])  # Displays the first two items using a slice.
print(my_list[0:4])  # Displays items at indexes 0 through 3.
print(my_list[-2])  # Displays the second-to-last item in the list.
print(my_list[-2:])  # Displays the last two items in the list.
print(my_list[:])  # Displays a shallow copy of the entire list.
print(my_list[::2])  # Displays every other item, starting with the first. used for skipping elements in the list.
my_list.append('new')  # Adds 'new' to the end of the list.
my_list.insert(2,'inserted')  # Inserts 'inserted' at index 2.
my_list.remove('DN')  # Removes the first matching 'DN' item from the list.
my_list.pop(3)  # Removes and returns the item at index 3.
print(my_list)  # Displays the list after its modifications.

my_list.reverse()  # Reverses the list in place. used for permanent
print(my_list)  # Displays the list after reversing it.

for i in reversed(my_list):  # Iterates over the list in reverse order. can be used for temporary use
    print(i)  # Displays each item in the reversed list

print(my_list[::-1])  # Displays the list in reverse order using slicing.
