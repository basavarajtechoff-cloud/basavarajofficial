#functions

def my_func(p_x):
    if (p_x > 10):
        print ("Greater than 10")  # Displays a message if p_x is greater than 10.
    else:
        print ("Less than or equal to 10")  # Displays a message if p_x is less than or equal to 10.

    return p_x

returned_value = my_func(25)  # Calls my_func with 5 and stores the returned value in returned_value.
print(returned_value)  # Displays the value returned by my_func when called with 5.

my_func(10)
my_func(20)

def my_func2(p_x,p_y):
    returned_value1 = p_x+p_y  # Returns the sum of p_x and p_y.
    print(returned_value1)

my_func2(10,20)  # Calls my_func2 with 10 and 20, but does not store or display the result.


def my_func3(*p_x):
    print(p_x)  # Displays the tuple of arguments passed to my_func3.
my_func3(10,20,30,40)  # Calls my_func3 with multiple arguments, which are captured in the tuple p_x.

def my_func3(**p_x):
    print(p_x,type(p_x))  # Displays the tuple of arguments passed to my_func3.
    print(p_x.keys())  # Displays the keys of the dictionary p_x.
my_func3(x=10,y=20,z=30,w=40)  # Calls my_func3 with multiple arguments, which are captured in the tuple p_x.

#lambda Function

addition=lambda x,y:x+y  # Defines a lambda function that takes two arguments and returns their sum.
print(addition(10,20))  # Calls the lambda function with 10 and 20, and displays the result (30).


#MAP, Filter and reduce 

my_list=[1,2,3,4,5,6]  # Creates a list of integers from 1 to 6.
new_list=list(map(lambda x:x*x,my_list))  # Uses map to apply a lambda function that squares each element in my_list, and converts the result to a list.
print(new_list)  # Displays the new list containing the squares of the elements in my_list.

def square(p_x):
    ret_list=[i*i for i in p_x]  # Creates a new list containing the squares of each element in p_x using list comprehension.
    print(ret_list)  # Displays the new list containing the squares of the elements in p_x.

    square(my_list)  # Calls the square function with my_list as the argument.
#map
def square(p_x):
        return p_x*p_x

result=list(map(square,my_list))

print (result)  # Displays the new list containing the squares of the elements in my_list using the square function.

#filter
def square(p_x):
    if(p_x%2==0):
        return p_x*p_x


result=list(map(square,my_list))
result1=list(filter(square,my_list))

print (result)
print (result1)

#reduce

from functools import reduce  # Imports the reduce function from the functools module.
def square(p_x,p_y):
    return p_x+p_y  # Returns the sum of p_x and p_y.

result3=reduce(square,my_list)

print (result3)  # Displays the result of reducing my_list by summing its elements using the square function.
