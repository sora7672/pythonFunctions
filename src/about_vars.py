# -*- coding: utf-8 -*-

"""
This is a little file for a little advanced knowledge to some basic things in python.
Can be multilines.
"""

"""
Maybe you know this as docstring, multiline comment or multiline string.
All these terms are correct.
Docstring = when it stands directly at top of a file, function, class or methode. It basically describes
what the programmer thought about the type its attached to.
Multiline string = When you set this onto a var like:
myvar = "multiline string"
Still need 3*" at start and end! But if you try to do it in here, you will exit the string again.
Multiline Comment = When its not a docstring or a multiline string, it will be ignored by python 
and thats why it is used for longer comments.
But most people still use this to comment stuff:
"""
# because many IDES(Integrated development editor)
# support easy commenting out multiple lines
# and do this with the hashtag (#)
# In pycharm thats done by holding ctrl(strg)+ divide on the numkeypad ( / shown as ➗)

# From now on i comment only as this :)


# First we need to advance you knowledge a little bit, to make this a little better readable
# dont worry! its super simple stuff!

# I will introduce you: "To your new best friend in coding!"
# The random module/library is normally in every python version already installed, so you just need to "import" it
# that means you load it in teh file. More about this you find in my modules & function examples.
# Here we stick to more basics

import random


# the second thing you need to know is that this is called a function call:
# function_name()      -> like print()
# functions are cruical for better code readability! And much better for testing.
# functions have names like "print" or "input" and  can have parameters, basically a var they want to get from you
# print("my name is sora")
# print -> function_name | () -> shows that its a function call, without it you cant execute it!
# "my name is sora" -> is a string variable, print for example also accepts other types like an int:
# print(25363)   -> same as ->
# mynumber = 25363
# print(mynumber)
# With this knowledge you now can create and call functions! More we wont need here.
# oh but functions can have multiple parameters also:
# print("my first string", "and another string")
# they are seperated through comma


# Below we created the first function and wrote a docstring
# (in pycharm you can see docstring documentation if you hover over a function/module/methode/class call)
def test_function():
    """
    This is the most simplistic function you can create.
    Instead of writting 3x print, you just do:
    test_function()
    """
    print("hello!")
    print("you!")
    print("how are you?")


# You have learned about the primitve datatypes:
# integer (int), float, boolean(bool), bytes
# maybe you have nt used bytes, thats why we test short what we can do with it

def about_bytes():
    a_bytes = b'hello'
    print(a_bytes.decode('utf-8'))  # This will just print the word hello, nothing new...
    # also notice you use for inline comments like above 2 spaces behind the codeline
    cool_bytes = b'\xe2\x80\xa0\xe2\x98\x85\xe2\x9c\x94'
    print(cool_bytes.decode('utf-8'))  # This will print some special chars ;)
    cool_text = b'\xe2\x98\x85Hello you! Look at this \xe2\x98\x85\xe2\x98\x85\xe2\x98\x85'
    print(cool_text.decode('utf-8'))  # This is a combination of text and some bytecode that prints stuff
    print(cool_text)  # No decode as check how it will look

    # to make it properly look, you need to decode the byte values.
    # you use the normal escape sign \ to show its no normal text
    # you can look all these byte infos up online, no need to learn it ;)


# bytes are for more advanced usages, but should at least be seen once.


# next we talk about non primitive data types
# (a string is in most languages a non primitive, thats why i include it here, but in python its a primitive)
# When you think about strings, you think first "a var that holds a text", but thats wrong.
# its list of characters! Thats why you can access strings with index operations.

def master_of_strings():
    my_string = "My name is sora. Im 33."
    print(my_string[::-1])  # This reverses the string

    # This below will gather all numbers in the string and makes a new string from it
    numbers = ""
    for char in my_string:
        if char.isdigit():
            numbers += char
    print(numbers)

    # We can also remove chars we dont want:
    with_removed_string = my_string.replace(".", " ").replace("  ", " ").strip(" ")
    print(with_removed_string)
    # strip removes ALL chars from a list (string is also a list) that are at start/end of the string, any order/amount

    # we can even split into words(with teh prepared string)
    words = with_removed_string.split(" ")
    print(words)  # This will show a list of the words

    # we can search for things in a string, but it will allways return the index of the startposition of  the search
    # because of that we added a integer value of the len-gth of the search text
    # if not found it returns -1
    index_found = my_string.find("name is ") + len("name is ")
    print(my_string[index_found:])
    # with one more step you can get only the name ;)

    # when we know the name length we could do this:
    print(my_string[index_found:index_found + 4])


# lists, tuples, dicts, sets, frozen sets, None


# before we continue to the more complex data types, here is smth. important we need to know for primitive ones:
# Type hinting, basically use ":" behind a variable and the typename to show what it should be
# in IDEs it can help you a lot with seeing usable methods or when you try to do smth. wrong
def changer():
    text: str = "Bananas"
    number_text: str = "1234"
    comma_text: str = "Karl,Franz,Max,Peter"
    female_names: list = ["Anna", "Susan", "Marry", "Paula", "Anna", "Kathrin"]
    car_types: tuple = ("Skoda", "VW", "Tesla", "Mercedes")
    # Type hinting in use, mostly you will see this in parameters of functions

    if type(text) is str:
        print(f"text is {type(text)}")
    if isinstance(text, str):
        print(f"text isinstance str: {isinstance(text, str)}")
    # Both work fine, but its recommended to take the isinstance,
    # specific when you work later with complexer data types from objects/classes!
    # This is so called Type Checking

    print(list(text))
    # this is type casting, which changes one type to another.
    # as explained before, a string is in general a list type
    # But be careful! not everything can be cast into every other type!
    #  Wont work -> int(text)    BUT:
    tmp = int(number_text)
    print(f"{type(tmp)} = {tmp}")
    # will work! Because all chars in number_text are digits, which can be one by one converted to an int

    male_names: list = comma_text.split(",")
    print(male_names)
    # above will basically create a list as we did with strings before

    # list can be exapanded, tuples on the other hand not.
    # so a set is the counterpart to list, only it can have NO DUPLICATED ENTRYS!
    # We could use this! Female names is not as we wanted it to be. It has dupes (duplicates)
    feme_fatal = set(female_names)
    print(feme_fatal)
    # but we need for another function a list :/ so we cast again:
    feme_fatal = list(feme_fatal)
    print(feme_fatal)

    # No we want all of the vars from before in one string for the next thing
    all_together = "" + text + number_text + comma_text
    for f in female_names:
        all_together += f
    for c in car_types:
        all_together += c
    print(all_together)
    # now we have a long text... We want to count each char. That we do with a dictionary trick!
    dict_chars: dict = {}

    # but we need to make all to uppercase before, because dicts are case sensitive!
    for char in all_together:
        if char.upper() not in dict_chars:
            dict_chars[char.upper()] = 1
        else:
            dict_chars[char.upper()] += 1

    print(dict_chars)
    # if you want, you can even sort that with a little more script (but i wont provide this here :P)


    # Lets look at the common practices with the None data type
    # it can be thought as Null from other languages or basically "there is no data here"
    # Most common it is used in function parameters to set their default to None
    # Thats to check for it or better prevent stuff to go haywire
def i_take_stuff(my_param: str = None):
    if my_param is None:
        print("there was no param given!")
    # Simple checks for None are done as above, you dont do "if var==None:" because None is a object,
    # which cant be allways compared like this. None is not "None", dont try to stringify it.

    text_to_split = my_param or "This is. a alternative. text"
    # Well there is shorthand ifs and this a use case for it. You can just use "or" for checking on a
    # None value. If my_param = None then use the alternative string
    # you could even chain this and its like normal program code top to bottom and left to right execution
    # that means the script takes the first value that is not None


    tmp_list = text_to_split.split(".")
    print(tmp_list)
    # You know this

    all_splits_mixed = [t.strip(". ").split(" ") for t in tmp_list]
    print(all_splits_mixed)
    # This is a list comprehension. Its like a shorthand for loop which can be executed in a list "[ ]" declaration
    # Our temp list is a list, so we want now to check on every element in that list and split it, before we remove
    # the unwanted spaces and dots at start & en of each list element, because else we get entries looking like "" this
    # This will sadly  result in a list in a list. So we need to work around that too

    all_splits = [entry for sublist in all_splits_mixed for entry in sublist]
    print(all_splits)
    # with this we used 2 list comprehensions in one list (in my opinion thats sometimes a little hard to follow
    # thats why i still prefer to write it in 2 loops)
    # and we have a list of our 2d list. And no we cant do "list(all_splits_mixed)" because its already a list


# Lets look into shorthand if's a little more, which is also known as "Ternary Operator"
def short_hands():
    empty = None
    number_high = 100
    number_low = 30

    # Lets use for this some random stuff (because its awesome!) Most simple thing to use:
    rndm = random.randint(1, 200)
    print(f"Random number is: {rndm}")
    # Create a random integer with the value of minimum 1 and maximum 200
    # as you know, parameters you can change! So we could also say 50 to 55 instead

    # This looks maybe confusing for a moment but if you follow the basic rules in programming  its easy to read
    # start from top to bottom, secondary code will be executed from left to right.
    # And as in math, brackets/parenthesis will be handled be executed before other stuff.
    bananas = 23 if rndm <= number_low else 100
    print(f"Number of Bananas: {bananas}")
    apples = 6 * (10 if rndm >= number_high else 5)
    print(f"Number of Apples:  {apples}")
    # Lets break it down:
    # at bananas it will write 23, but only when the if check is true.
    # Means if rndm is smaller equal number_low its true
    # if its not true the else statement will be executed, which will set the value to 100 there
    # apples is the same, but because it involves a "execution" behind the equal sign,
    # you need to put it between parenthesis, else it will either execute the 6*10 as value or set the value to 5
    # but we intended here to multiply the 6 with either 10 or 5, thats why we need parenthesis here.



    complex_stuff = empty or "Trees are awesome" if rndm <= (number_high + number_low) else "We dont like onions"
    print(complex_stuff)
    # Here we combined that we know, "or" on a None value will replace it and shorthand if
    # but we combined in the if check (using parenthesis) a execution before the check, which adds 2 vars together
    # in easy translated: if "empty" is None, replace it with "trees..." if rndm is smaller than 130,
    # if not fill it with "...onions"


    # here we go with our random friend. We create 8 random values (and add a list that only has "0" in it)
    # with a list comprehension. Thats some pretty common use for testing out things.
    check_nums = [random.randint(-10, 10) for _ in range(8)] + [0]
    result_list = ["Positive" if n > 0 else "Negative" if n < 0 else "Zero" for n in check_nums]
    for index in range(len(result_list)):
        print(f"{check_nums[index]} is {result_list[index]}")
    # We used for result list a combination of list comprehension (which executes a number of times, 
    # based on the iterable the code before it) and let it execute a if for every element in the lsit
    # Basically we used here 2 ifs. That only works, when there cant be a combination of true reults:
    # Zero cant be positive or negative | Positive cant be zero or negative | Negative cant be zero or positive
    # if we would ignore the zero case, we will have a smaller list, which will result in an error
    # or better not print logically as we wanted it.



# You see now, why i used functions. Otherwise it would be super annyoing to test/read
# and understand what we do in this bigger file for someone new.
# Together with the input you should know by now, you can allready write pretty complex programs now!
# HAPPY CODING!

# Here you can test every function from above ;)
# Just do as explained above: function_name(parameter, parameter2) | or h
# i added all functions as comment, so just uncomment them to test each ;)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # #  TEST AREA BELOW! # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# test_function()
# about_bytes()
# master_of_strings()
# changer()
# i_take_stuff()
# i_take_stuff("This.is.my.new.test.string!")

# i_take_stuff("another string wth much stuff", "and a error")
# WARNING! This will result in an error! Because it took 2 parameter (seperated through ",") and only accepts 1!

# short_hands()
