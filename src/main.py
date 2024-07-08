import random

# This is a build in function of python
print("Hello World")

# This is a function i created (or better this is how its created)
def my_hello():
    print("Hello Sora")

# This calls our new created function
my_hello()


# this loads my own new script (please NOTE that you allways write the imports at the top of the file!)
import external_functions
# and this is how you call my new own function from another script
external_functions.my_external_hello()

# to import a script, you allways need to go the way from your file.
# We are in src, but the script we want is in "sub"
import sub.snake
# to call it you also need the folder before
sub.snake.awesome_print()

# a smarter way is to import "as", to call it with less text
import sub.snake as bro
# calls it with the name we gave it
bro.awesome_print()

# you can even import only one specific function from another module with the "from" keyword
# and set a substitute for the function call
from sub.snake import awesome_print as aprint
aprint()


# also a site note! when you call functions with the "." between, its because thats part of OOP of python
# imagine is as "object.methode()" a string is a class, when you created a string variable
# the variable is a object of the class string
# because of that you can do the following:
mystring = "abcdefgh   !!!"
mystring.replace("!", " ").replace(" ", "").replace("cd", "AA")
# basically this is object.method() <- returns an object so you can object.method().method() ....
# and so on. Methods can change the object they are called on, thats why you can line them up like this

int(12).as_integer_ratio()
# this creates a object of class integer, so we cant use .replace(), because the class ineteger has
# no such method. The same goes for a string object, it cant call ".as_integer_ratio()" because that belongs to int class
# end of little explanation of classes& objects (that we talk about next time)

# this also loads the same file, but with another reference name
import external_functions as ext
# and this calls another function in the same file, based on reference name
ext.second_hello()

# functions are there for a few reasons.
# 1. to prevent code duplication (instead of having x times the same 10 lines of code, you create a function
# 2. for better readability of your code
# 3. for better scalability (you can change one function instead of multiple areas in your project)
# 4. for others to be able to easyer understand what your code does. (docstrings and type declaration)

# functions can also return values
def one_hundred():
    return 100
# this will just print the return value of a function
print(one_hundred())

# some inside info, every function can return stuff and/or do stuff. Limitied to your imagination
def pseudo_return():
    print("I am a pseudo return")
    return "This is my return value"
# even if a function returns something, you DONT need to do smth with it!
# this will just do stuff and print but not return
pseudo_return()
# and this does the same as above, but also saves the return in a variable
pseudo_var = pseudo_return()

# functions can also return multiple values! or iterables or objects (more to this later)
def my_fav_numbers():
    return 13, 33, 77, 186

print(my_fav_numbers())

# functions can take in zero to infinite arguments(called parameter which has a value) also.
def calc_sum(a,b):
    return a+b

print(calc_sum(3,2))

# even better, you can set default values of parameters
def book_print(bookname, author, number_pages=10):
    print(f"{bookname} by {author} with {number_pages} pages")

book_print("Bananas in pijamas", "Sora")

# This is about how you can call function parameter also
def my_list(item1, item3, item4, item2):
    return [item1, item2, item3, item4]
# as you see the order you place in arguments does matter if you dont call them by parameter name
print(my_list(1,item2=2,item3=3,item4=4))
print("compare to this:")
print(my_list(1,2,3,4))
# if you place the parameters without declaring to which variable it belongs, it will take the order
# of how the function has declared them.

# this function is an example of a simple recursion, means a function calls itself till its on its "escape" point
def sum_till_x(x):
    if x <= 1:
        return 1
    else:
        return x + sum_till_x(x-1)

# the upper function call does the same as the print below, but we can changeb the parameter of that function
print(sum_till_x(5))
print(5+4+3+2+1)
# this is used in programming, to minize the functions needed. They are only in specific cases needed!

# till now all functions accept all type of parameters, but if we want to work properly with functions
# we should define what type of parameter we want.

def sub_nums(a:int,b:int):
    return a - b
# simple right? That can also be done outside of functions. Just varname:vartype
test_num:int = 21

# thats still not enough to have a proper looking function. We want to declare the return type also
def multi_nums(a:int,b:int) -> int:
    return a * b
# with the -> after the parameter input parenthesis and before the : we declare the return type
# check this in your IDE with hovering over the function name, there you see now the help about a function.


# so here is the best way to create a function
def randomize_chars(in_text: str) -> str:
    """
    This function takes a string and mixes the chars \n
     random and returns that string
    :param in_text: str
    :return: str
    """
    out = ""
    o_list = list(in_text)
    random.shuffle(o_list)
    for i in o_list:
        out += i

    return out
# now hover over the "randomize_chars" in you IDE to see the whole description
# also hover over the function .shuffle() in the function and see the description (it even has a link to more details!)
print(randomize_chars("abcdefghijkllmnop"))

