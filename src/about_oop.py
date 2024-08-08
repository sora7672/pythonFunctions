
import random


print(random.randint(0, 1))
# Call the class random with method randint() -> class.method() or object.method()
# Methods are functions INSIDE a class
# variables inside of a class are called attributes


class MyTestClass():
    def __init__(self):
        self.field = random.randint(1, 100)


# here we define our first class and give it a "self" value, which is allways bound to the instance/object.
# the self is a placeholder for the object/instance that is calling the method

myobject1 = MyTestClass()
myobject2 = MyTestClass()
myobject3 = MyTestClass()

# to create an object/instance you need to just call the classname()

print(myobject1.field)
print(myobject2.field)
print(myobject3.field)

# as you see, different objects can have different values in the same attribute (here its field)


x = 5
mylist = []
mylist.append(x)
mylist.append(MyTestClass())
print(mylist[1].field)

# you dont need to bind the object, same as vars, onto a var. so you could also add it directly to a list
# or another class! (later specific infos)


class SecondaryClass():
    def __init__(self, name, age: int = None):
        self.name = name

        if age is not None:
            age = int(age)
        else:
            self.age = random.randint(1, 35)

# here we defined another class, as you see here its again PascalCase(CamelCase) from the uppercase letters
# its standard that classes start with a Capital letter and you use for each word in it also a capital letter

# the __init__() is a special method that almost every class needs.
# it basically is creating the object that is created with MyClass()
# also __init__ can be handled like a normal function, so you can give as many parameters further as you want. But!

second = SecondaryClass("Bob")
print(second.name,second.age)

# this are all public attributes. You can access them with object.attribute
#as you see, if you use positional parameters, you need to use them to call/create the class too! If you use keyword
# parameters and set a default value, you dont need to call that allways (examples follow later)
print("----------- TREES -------------")
class Tree():
    def __init__(self):
        self._height = 100
        self.__leaves = 300


    def get_height(self):
        return self._height

    def get_leaves(self):
        return self.__leaves

    def set_height(self, height):
        self._height = height

    def set_leaves(self, leaves):
        self.__leaves = leaves



# if you dont use "_" or "__" before a method/property the standard is that these are public, which means, you can
# or better in python you are allowed to, access these attributes directly from the object.
# in this case we use "_" that for a proctected property, which means "you should not" access it from the outside
# we step now into inheritance(parent and child classes) where we need these modifiers.
# A protected property/method can be accessed by the childclass also.
# Same goes for public methods/attributes
# the "__" defines a private attribute/method, they can only be accessed from inside the class(not in childs)

oak = Tree()
oak._height = 1000
print("myoak", oak._height)
# you can access protected methods/attributes from the outside
# The programmer never defined it without reason as protected! (if in any case you need to read it, ok...
# BUT! You should Never change the values! Normaly protected attributes are generated with functions.
# so it could be that there is a dependency on other attributes to calculate the value of a protected attribute.

# print("oak wrong calls:",  oak.__leaves)
# if you try to access the attributes that are either private in a class, you get an error.
print("oak", oak.get_height(), oak.get_leaves())
# thats why you need to properly get the values of protected and private attributes/methods.


print("--------------")
class Birch(Tree):
    def __init__(self):
        super().__init__()
        print(self._height)
        # you have access to protected attributes of the parent

    def test_leaves(self):
        #print("leaves:",self.__leaves)
        # here you see, that you dont have access to private attributes of the parent class Tree
        pass

mybirch = Birch()

print("mybirch", mybirch.get_height(), mybirch.get_leaves())
mybirch.test_leaves() # not working because __leaves is private from class Tree

# as you see you to create a child of a parent class yu need to define the parent class like this:
# class ChildClass(ParentClass):
# and the __init__ needs to call the init of the parent. That you do with "super()" which calls the parent
print("----------- ENEMIES -------------")
class Enemies():
    __list_enemies = []
    def __init__(self, name, type):
        self.name = name
        self.type = type
        Enemies.__list_enemies.append(self)


    @classmethod
    def get_list_enemies(cls):
        return cls.__list_enemies

# This is some advanced stuff now. You have  different
# DECORATORS
# in python, that can change the handeling of methods
# here we used a classmethod, which is NOT bound to the object/instance!
# instead you need to call it on the class.
# if you define a attribute inside the class (not a method with

gob = Enemies("Gobuta", "Goblin")
rimuru = Enemies("Rimuru", "Slime")

print(Enemies.get_list_enemies())
print(gob.get_list_enemies())

# As you see, you can define attributes inside the class directly, they are not bound to an object but
# can be also called from an object. This is helpfull to access stuff between objects or save objects into
# a list like here.

class Goblin(Enemies):
    __army = 0
    def __init__(self, name):
        super().__init__(name, "Goblin")
        self.level = 0
        Goblin.__army += 1
        # only working because we are inside the class Goblin

    def levelup(self):
        self.level += 1

    @staticmethod
    def get_goblins():
        gobsys = []
        for enemy in Enemies.get_list_enemies():
            if enemy.type == "Goblin":
                gobsys.append(enemy)
        return gobsys

    @staticmethod
    def test_class_attribute_get():
        try:
            print(cls.__army)
        except Exception as err:
            print(err)
        try:
            print(self.__army)
        except Exception as err:
            print(err)
        try:
            print(__army)
        except Exception as err:
            print(err)

        finally:
            print("End of class attribute test")

    @classmethod
    def get_army_number(cls):
        return "Army of " + str(cls.__army) + " existing"

# Here we created a child class based on enemys
# we use now a staticmethod. Static means its called by the class BUT you dont have access to cls (class) attributes!
# So we called in here the Enemies classmethod to get all created Enemies and filter them.
# the second static method is to show you, what is not possible with static methods.
# But you could (means you should not) access it via Goblin.__army , its a much clearer style to use cls.__army
# Python is special in this, you can do a lot, in other languages its much stricter and access limited,
# where you really need to live the OOP principles.

print("---- GOBLINS ----")
print(Goblin.get_goblins())

hobo = Goblin("Maso")

print(Goblin.get_goblins())
print(Goblin.test_class_attribute_get())
print(Goblin.get_army_number())


# Now we need smth. imported, thats why we do it here, also when correct style is on top of file!
from abc import ABC, abstractmethod
# ABC = abstract base class
print("----------- Abstraction and inheritance-------------")

class Interactable(ABC):
    def __init__(self, living):
        self.__living = living
    @abstractmethod
    def destroy(self):
        pass

class Living(Interactable):

    def __init__(self):
        super().__init__(True)
        self._is_alive = True

    def destroy(self):
        self.death()

    def death(self):
        self._is_alive = False
        print(self, " Died!")

    @abstractmethod
    def move(self, direction:str):
        pass



# Till here explained:
# abstract means it has no functionality /context, so its basically like a placeholder for further Childs
# By using the IMPORTED @abstractmethod decorator, we tell the script "Hey if you create childs, you ABSOLUTLY need
# to create this method and do smth!"

print("----------- CowOld example -------------")
# we called it CowOld because we later use Cow
class CowOld(Living):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._x_position = 0
        self._y_position = 0

    def move(self, up=False, down=False, left=False, right=False):
        num_keys = int(up) + int(down) + int(left) + int(right)
        if num_keys == 0:
            print("Error! You didnt tell the cow",self._name,"where to move")
        elif num_keys > 1:
            print("Error! You cant tell the cow",self._name,"to go into multiple directions at once!")
        else:
            if up:
                self._y_position += 1
                print(self._name,"moved up")
            if down:
                self._y_position -= 1
                print(self._name,"moved down")
            if right:
                self._x_position += 1
                print(self._name,"moved right")
            if left:
                self._x_position -= 1
                print(self._name,"moved left")

    def eat(self, food):
        eatables = ["grass", "wheat", "hay", "leafs", "bugs"]
        if food.lower() in eatables:
            print(self._name,"ate", food)
        else:
            if random.randint(0,1) == 1:
                print("NO! You gave",self._name, food, "and it ate it!")
                self.death()
            else:
                print(self._name,"dont like", food, "and didnt eat it. Lucky you!")

# Now we created smth. that could actually be a thing to work with
# we reached our "final" class here, where we implemented the abstract methods.
# The Cow class has only one parent class, so we can init it with super().__init__() again
# We also added a move function and some attributes to use it with.
# and you can even feed your cow!
# But if the cow eat smth. bad it can happen, that it calls the parents "Living".death() method

martha = CowOld("Martha")

martha.move(up=True)
martha.eat("hay")
martha.move(right=True)
martha.eat("mushroom")



# We created a new instance of a cow, called martha. Then tryed to move her and feed her to see if all this works
# We used on feed the death/ destroy method from the parent class living (only in 50% of cases where you fed smth wrong)


# This looks more complex than it is, its just a lot code, but you know almost all it does.
# Take your time to read it and check the description below

print("----------- Creating classes with inheritance -------------")
class NonLiving(Interactable):
    def __init__(self):
        super().__init__(False)

    def destroy(self):
        print("Destroyed object: ", self)


class Barn(NonLiving):
    def __init__(self, x_start: int = None, x_end: int = None, y_start: int = None, y_end: int = None):
        super().__init__()
        self.__animal_list = []
        if x_start is None:
            self._x_start = 0
        else:
            self._x_start = x_start

        if x_end is None:
            self._x_end = 0
        else:
            self._x_end = x_end
        if y_start is None:
            self._y_start = 0
        else:
            self._y_start = y_start
        if y_end is None:
            self._y_end = 0
        else:
            self._y_end = y_end

        # set the minimum size of the barn to 10 (only working wth positive values)
        x_size = self._x_end - self._x_start
        y_size = self._y_end - self._y_start
        if x_size < 10:
            self._x_end += 10 - x_size
        if y_size < 10:
            self._y_end += 10 - y_size

    def destroy(self):
        print("Destroyed object: ", self)
        if len(self.__animal_list) >=1:
            print("Oh no you killed also the animals:")
            for animal in self.__animal_list:
                print(animal.name, "(" + type(animal) + ")")
                animal.death()

    def pos_in_barn(self, pos_x, pos_y):
        if self._x_start < pos_x < self._x_end and self._y_start < pos_y < self._y_end:
            return True
        else:
            return False

    def middle_of_barn(self):
        x_size = self._x_end - self._x_start
        y_size = self._y_end - self._y_start

        return (self._x_end - x_size/2, self._y_end - y_size/2)

    def add_animal(self, animal):
        self.__animal_list.append(animal)
        x,y = self.middle_of_barn()
        animal.set_position(x,y)

    def get_animals(self):
        return self.__animal_list

# We now created a barn where we can store our animals and they can move around!
# This code is not perfect! There is a lot you should do in your real classes, which i didnt do now.
# (like input validation and commenting it properly)


class Animal(Living):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._x_position = 0
        self._y_position = 0

    def __str__(self):
        return f"{self._name} of class {type(self)}"
    def destroy(self):
        self.death()

    def death(self):
        self._is_alive = False

    @property
    def position(self):
        return self._x_position, self._y_position

    def set_position(self, x, y):
        self._x_position = x
        self._y_position = y

    def move(self, direction: str):
        """

        :param direction: UP, DOWN, LEFT, RIGHT
        :return:
        """
        if self._is_alive == False:
            print("Dead bodys cant move on their own!")
            return None
        match direction.upper():
            case "UP":
                self._y_position += 1
                print(self._name,"moved up")
            case "DOWN":
                self._y_position -= 1
                print(self._name,"moved down")
            case "RIGHT":
                self._x_position += 1
                print(self._name,"moved right")
            case "LEFT":
                self._x_position -= 1
                print(self._name,"moved left")
            case _:
                print("Error! You didnt tell the animal correct where to move to!")
                print("(UP, DOWN, LEFT, RIGHT)")

    def eat(self, food):
        if self._is_alive == False:
            print("Dead bodys cant eat")
            return None
        eatables = ["grass", "wheat", "hay", "leafs", "bugs", "bork"]
        if food.lower() in eatables:
            print(self._name,"ate", food)
        else:
            if random.randint(0,1) == 1:
                print("NO! You gave",self._name, food, "and it ate it!")
                self.death()
            else:
                print(self._name,"dont like", food, "and didnt eat it. Lucky you!")

# here we used 2 new things. The first is __str__ which basically is an internal override for what
# we see if we use "print(animalObject)", like more customized info about the class.
# the second is the @property decorator, it can be used on methods to call them like this:
# "myObject.myProperty" without using the () in the end for a method.
# it depends on personal preference if you want to define it like this or with self.myProperty
# if you need to calculate smth. for your return, you need the decorator for property or a normal method call
# And the move() function used a return as escape sequence, if the animal is dead, same as eat()


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    pass


class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self, direction: str):
        """

        :param direction: UP, DOWN, LEFT, RIGHT
        :return:
        """
        if self._is_alive == False:
            print("Dead bodys cant move on their own!")
            return None
        match direction.upper():
            case "UP":
                self._y_position += 2
                self._x_position -= 1
                print(self._name, "moved up")
            case "DOWN":
                self._y_position -= 2
                self._x_position += 1
                print(self._name, "moved down")
            case "RIGHT":
                self._x_position += 2
                self._y_position -= 1
                print(self._name, "moved right")
            case "LEFT":
                self._x_position -= 2
                self._y_position += 1
                print(self._name, "moved left")
            case _:
                print("Error! You didnt tell the animal correct where to move to!")
                print("(UP, DOWN, LEFT, RIGHT)")
    pass

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self, direction: str):
        """

        :param direction: UP, DOWN, LEFT, RIGHT
        :return:
        """
        if self._is_alive == False:
            print("Dead bodys cant move on their own!")
            return None
        match direction.upper():
            case "UP":
                self._y_position += 3
                print(self._name, "moved up")
            case "DOWN":
                self._y_position -= 3
                print(self._name, "moved down")
            case "RIGHT":
                self._x_position += 3
                print(self._name, "moved right")
            case "LEFT":
                self._x_position -= 3
                print(self._name, "moved left")
            case _:
                print("Error! You didnt tell the animal correct where to move to!")
                print("(UP, DOWN, LEFT, RIGHT)")
    pass

# what we saw here now is a example of polymorphism, means child classes override methods/propertys
# from parent class. (Specific heere propertys because they are methods also)
# You see all different animals have different movement patters, but still you call them Animal.move(direction)
# They all inherited the attributes like x/y from the parent animal.

# lets use the barn properly:
print("----------- My little FARM -------------")
my_little_farm = Barn(10,40, 15,60)
ani = Horse("Tina")
my_little_farm.add_animal(ani)
my_little_farm.add_animal(Horse("Horst"))
my_little_farm.add_animal(Goat("Betty"))
my_little_farm.add_animal(Cow("Milka"))
print(my_little_farm.get_animals())

# now we have a barn with animals! What are we doing with it now?
# we can get the animals on the farm.

for animal in my_little_farm.get_animals():
    print(animal._name) # dont use this, its just for show


def feed_all(self):
    food_on_barn = ["grass",  "meat", "wheat", "hay", "leafs", "bugs", "bork", "poop"]
    for animal in self.get_animals():
        ran_food = random.choice(food_on_barn)
        animal.eat(ran_food)

my_little_farm.feed_all_animals = feed_all

my_little_farm.feed_all_animals(my_little_farm)

# here we added a new method to the INSTANCE not the class or other objects of this class.
# so if we use another barn we cant use the method.
print("----------- DIRKS FARM -------------")
dirks_farm = Barn(110,140, 35,88)

dirks_farm.add_animal(Horse("Beate"))
try:
    dirks_farm.feed_all_animals(dirks_farm)
except Exception as err:
    print(err)

# as you see you cant call it from another instance of barn
# so how we add it to the class later?

Barn.feed_all = feed_all

# now we added the feed_all() function to the class itself!
# NOTE: if you access the class directly, you need to call the name properly (case sensetive)
# if we try again now with the new call:

try:
    dirks_farm.feed_all()
except Exception as err:
    print(err)

# if you use pyCharm you see the resolve warning, but that does not matter. Its  a bad style to add
# a method to a class or instance like this. Properly add it to a class on creation if possible
# also the barn and animal concept is an example of Aggregation in OOP, meaning one object can have a "weak relation"
# to other objects/classes. If there is no barn, the animals can still exist

print("----------- Special methods -------------")

class Arabian(Horse):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Arabian"

    def __str__(self):
        return f"{self._name} is Arabian breed"

    def __repr__(self):
        return f"name:{self._name}, breed: {self.breed}, position: ({self._x_position, self._y_position}), is_alive: {self._is_alive}"


class FriesianHorse(Horse):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Friesian Horse"

    def __str__(self):
        return f"{self._name} is Friesian Horse breed"

    def __repr__(self):
        return f"name:{self._name}, breed: {self.breed}, position: ({self._x_position, self._y_position}), is_alive: {self._is_alive}"


arab = Arabian("Peppe")
fries = FriesianHorse("Meike")

print(arab)
print(fries)
print("Compared to:")
print(repr(arab))
print(repr(fries))


# here we have some Dunder(maic) methods. Dunder = d-double under-score
# the __str__ dunder method is used for informal return of the instances, like print(myHorse) or str(myHorse)
# the counterpart is the __repr__ which is used for smth. like stacktracing & debugging used like repr(myHorse)
# There is also the option on each class to change the behaviour of operators (Operator Overloading) like
# Arithmetic Operators "+-*/" | Comparison Operators (= != < >) | Unary Operators (- + abs() ~) |
# Container Methods for setting/getting behaviour of lists & similiar -> to many to explain short
# there is also __iter__ & __next__ which can create a object as iterable, like specific type of list
# and set the behaviour for iterating through the object




print("----- Composition classes -----")


class Carnivore:
    def __init__(self):
        self.eatables = ["meat", "chicken", "deer", "cow", "sheep", "carcass", "bone", "human"]


class Herbivore:
    def __init__(self):
        self.eatables = ["leaf", "leaves", "grass", "wheat", "mushroom", "fruit", "veggie", "bork"]


class Wolf(Carnivore, Animal):

    def __init__(self, name="Wild Animal"):
        Animal.__init__(self,name)
        Carnivore.__init__(self)

    def eat(self, food):
        if not self._is_alive:
            print(f"({type(self)})","Dead bodys cant eat")
            return None

        if food.lower() in self.eatables:
            print(self._name,f"({type(self)})","ate", food)
        else:
            if random.randint(0,1) == 1:
                print("NO!",self._name,f"({type(self)})","ate", food)
                self.death()
            else:
                print(self._name,f"({type(self)})","dont like", food)


class Bunny(Herbivore, Animal):
    def __init__(self, name="Wild Animal"):
        Animal.__init__(self,name)
        Herbivore.__init__(self)

    def eat(self, food):
        if not self._is_alive:
            print(f"({type(self)})","Dead bodys cant eat")
            return None

        if food.lower() in self.eatables:
            print(self._name, f"({type(self)})","ate", food)
        else:
            if random.randint(0, 1) == 1:
                print("NO!", self._name,f"({type(self)})", "ate", food)
                self.death()
            else:
                print(self._name, f"({type(self)})","dont like", food)

foodlist = ["leaf", "leaves", "grass", "wheat", "mushroom", "meat",  "carcass", "bone"]

hopedy = Bunny()
silver = Wolf()
silver.eat(random.choice(foodlist))
hopedy.eat(random.choice(foodlist))

# Here we created Composite classes, meaning a class that inherited multiple classes.
# Thats possible in python, but not other languages. You cant use super().__init__ .
# To init the correct parent class we need to use "Classname".__init__(self)
# (There is a complicated way to make one class parent the main parent which you could call then
# with super() but we wont look at it here.)
# You use composites to save time and not copying code fragments. In the sense of Code Reusability and
# DRY (Dont repeat yourself)
# Also here we use overriding of the method Living.eat() and .move() to have a proper display and test
# which shows the Polymorphism principle

print("---- Type Annotations & Docstrings ----")

class Teacher:
    """
    Innitialize the Teacher class with a name:str, age:int and male:bool \n
    """
    def __init__(self, name: str, age: int, male: bool):
        self.name: str = name
        self.age: int = age
        if male:
            self.gender: str = "Male"
        else:
            self.gender: str = "Female"

    def reputation(self):
        """
        Tells you a random reputation for that teacher
        :return: str
        """
        if random.randint(0, 1) == 1:
            return f"{"Miss" if self.gender == "Female" else "Mister"} {self.name} ({self.age}) is a good teacher!"
        else:
            return f"{"Miss" if self.gender == "Female" else "Mister"} {self.name} ({self.age}) is a bad teacher..."

# its pretty important that you properly describe your class and attributes.
# because you create classes which should be used again and again and you dont want to allways jump
# back into the file where yu define your class. Normally you create classes in extra files, which
# are not allways open, so if you use a good IDE like pyCharm you can check the type hinting or description of
# the methods/class

print("---- Data Classes & propertys----")

from dataclasses import dataclass, field

@dataclass
class Stats:
    """
    Takes as creation parameter:\n
    Stat(strength, stamina, agility)

    Available getter only properties:\n
    attack, health, speed\n
    Getter & Setter properties:\n
    strength, stamina, agility
    """
    _strength: int = field(default=0)
    _stamina: int = field(default=0)
    _agility: int = field(default=0)

    # Private attributes for computed values
    __attack: int = field(init=False, repr=False)
    __health: int = field(init=False, repr=False)
    __speed: int = field(init=False, repr=False)

    def __post_init__(self):
        """Initialize computed properties after the main attributes."""
        self._update_computed_properties()

    def _update_computed_properties(self):
        """Update the computed properties."""
        self.__attack = round(self._strength * (0.3 * self._agility))
        self.__health = round(self._stamina * (0.4 * self._strength))
        self.__speed = round(self._agility * ((self._stamina - self._strength) * 0.3))

    @property
    def attack(self) -> int:
        """Getter for attack."""
        return self.__attack

    @property
    def health(self) -> int:
        """Getter for health."""
        return self.__health

    @property
    def speed(self) -> int:
        """Getter for speed."""
        return self.__speed

    @property
    def strength(self) -> int:
        """Getter for strength."""
        return self._strength

    @strength.setter
    def strength(self, value: int) -> None:
        """Setter for strength with validation."""
        if value <= 0:
            raise ValueError("Strength cannot be negative or 0")
        self._strength = value
        self._update_computed_properties()

    @property
    def stamina(self) -> int:
        """Getter for stamina."""
        return self._stamina

    @stamina.setter
    def stamina(self, value: int) -> None:
        """Setter for stamina with validation."""
        if value <= 0:
            raise ValueError("Stamina cannot be negative or 0")
        self._stamina = value
        self._update_computed_properties()

    @property
    def agility(self) -> int:
        """Getter for agility."""
        return self._agility

    @agility.setter
    def agility(self, value: int) -> None:
        """Setter for agility with validation."""
        if value <= 0:
            raise ValueError("Agility cannot be negative or 0")
        self._agility = value
        self._update_computed_properties()

    def __repr__(self) -> str:
        return (f"Stats(strength={self._strength}, stamina={self._stamina}, "
                f"agility={self._agility}, attack={self.__attack}, "
                f"health={self.__health}, speed={self.__speed})")

    def __str__(self) -> str:
        return (f"BaseStats(strength={self._strength}, stamina={self._stamina}, "
                f"agility={self._agility}) Calculated Stats(attack={self.__attack}, "
                f"health={self.__health}, speed={self.__speed})")



status = Stats(5, 10, 12)
print(status)

# This is much code. Dont be scared of it. Its basically pretty simple. All it does
# is some simple math and returns values and saves values.
# This is a data class, which is created differently than normal classes, because its has
# an override __init__ method that is acutualy called automatically.
# YOu use this to define that its only saving and returning attributes or in this case
# properties which are a specific kind of method that can be called like "object.property"
# To define setters you use @propertyName.setter -> @strength.setter
# the normal @property can be thought as "getter"
# the data class also changes standard behaviours like comparsion (if objectA == objectB)
# if you normally compare objectA with objectB you compare the "memory" area, where the object is saved
# which is allways different, except ist THE ABSOLUTE SAME object.


print("---- Dataclass objects in another class ----")
class Monster(Living):
    def __init__(self, stat_object: Stats = None):
        super().__init__()
        self.breed = None
        self._x_position = 0
        self._y_position = 0
        if stat_object is None:
            new_stats = Stats(
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20))
            self.stats = new_stats

        else:
            self.stats = stat_object

    def move(self, direction: str):
        """

        :param direction: UP, DOWN, LEFT, RIGHT
        :return:
        """
        if not self._is_alive:
            print("Dead bodys cant move on their own!")
            return None
        match direction.upper():
            case "UP":
                self._y_position += round(self.stats.speed*0.1) + 1
            case "DOWN":
                self._y_position -= round(self.stats.speed*0.1) + 1
            case "RIGHT":
                self._x_position += round(self.stats.speed*0.1) + 1
            case "LEFT":
                self._x_position -= round(self.stats.speed*0.1) + 1
            case _:
                print("Error! You didnt tell the monster correct where to move to!")
                print("(UP, DOWN, LEFT, RIGHT)")


class Oger(Monster):
    def __init__(self, stat_object: Stats = None):
        super().__init__(stat_object)
        self.breed = "Oger"
        self.stats.strength = round(self.stats.strength * 1.5)
        self.stats.stamina = round(self.stats.stamina * 2)
        self.stats.agility = round(self.stats.agility * 0.2)


mr_oger = Oger()
print(mr_oger.stats)

miss_oger = Oger(Stats(8, 15, 50))
print("miss oger: \n", miss_oger.stats)

copycat = Oger(mr_oger.stats)
print("Im a copy of mr oger's stats at this moment:")
print(copycat.stats)

# to make it easyer for further "Monster"s we created a parent class with base things
# there we added a object Stats to it, so we have access to all the things we need.
# we either take random values on creation or use a given Stats object
# if we now change how the stats are buildup/ calculated, we only need to change
# that in the Stats class, not any Monster later that inherited from Monster class.
# we can simply access the Stats object like this:
# my_monster.stats and have access to all the attributes & propertys of that class like:
# my_monster.stats.attack or my_monster.stats.stamina



# After we created a new class Oger that gets all from Monster class
# Then we changed the Stats class in the init process of the object Oger to fit our "Oger" needs.
# We could create on the "blueprint" of monster now infinite classes and use this classes
# for subclasses(like stronger or weaker maintype variants)

# there is also a lot of other topics you could/should at least look into once for widen your knowledge.
# this are some things i stumbled upon: Metaclass, Mixins, Slots (__slots__)


print("###END###")
