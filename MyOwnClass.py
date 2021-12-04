# Neha Zope
#Assignment 10.1: Your Own Class
# this code will implement my own class based ona real-world object(I chose a regular cup for drinking liquid). 
#resources used:
    #I used the lecture slides 7.3 to understand encapsulation and how to do get-set methods
    #used https://www.tutorialspoint.com/python3/python_basic_operators.htm to know the logical operator or to use in my methods

#creating a class called Cup
class Cup:
    #every cup has an opening to drink from therefore this is a class variable
    has_opening = True
    #def __init__ within the class
    def __init__(self, size = "small", type = "plastic"):
        #setting up data variable self.__size for the sizes of the cup
        self.__size = size
        #using the set_size method to ensure there is an error if the size in the init is not small, medium, or large
        self.set_size(size)
        #setting up data variable self.__type for the types of cups
        self.__type = type
        #using set_type method to ensure there is an error if the type is not plastic, wood, china, steel, or glass
        self.set_type(type)

    #define the set_size method
    def set_size(self, size):
        #size can only be small, medium, or large in this class
        #if the size is one of the listed, then set size as self.__size(private variable)
        if size == "small" or size == "medium" or size == "large":
            self.__size = size
        #if the size is not one of the listed, print an error and it should show None
        else:
            print("Error. Not a valid size. Size has to be a string of only either small, medium, or large.")
            self.__size = None
    #define the get_size method
    def get_size(self):
        #this is returning what the new set_size is, if user did not create a new size, it will return the original
        return self.__size

    #define the set_type method
    def set_type(self, type):
        #type can only be plastic, wood, china, steel, or glass
        #if the type is one of the listed, then set it as self.__type(private variable)
        if type == "plastic" or type == "wood" or type == "china" or type == "steel" or type == "glass":
            self.__type = type
        #if the type is not one of the listed, then print an error and it should show None
        else:
            print("Error. Type of cup has to be a string of only either plastic, wood, china, steel, or glass.")
            self.__type = None
    #define the get_type method
    def get_type(self):
        #this is returning what the new set_type is, if user did not create a new type, it will return the original
        return self.__type

    #define cup_volume method
    def cup_volume(self):
        #if the cup size is small
        if self.__size == "small":
            #the volume of the cup is total 8oz, meaning it can hold 8oz of liquid
            self.__volume = "8oz"
            return self.__volume
        #if the cup size is medium
        elif self.__size == "medium":
            #the volume of the cup is total 12oz, meaning it can hold 12oz of liquid
            self.__volume = "12oz"
            return self.__volume
        #if the cup size is large
        elif self.__size == "large":
            #the volume of the cup is total 16oz, meaning it can hold 16oz of liquid
            self.__volume = "16oz"
            return self.__volume
        #if the size initially is not one of the listed, then print an error
        else:
            print("Error. Not a valid size. Size can only be small, medium, or large.")


    #define which_drinkswork method
    def which_drinkswork(self):
        #if the cup type is plastic or wood
        if self.__type == "wood" or self.__type == "plastic":
            #cannot have hot liquids such as coffee or tea(as the heat will eventually make wood crack and plastic would melt into the drink)
            self.__drinkswork = "No hot liquids(such as coffee or tea) work with this type of cup."
            return self.__drinkswork
        #if the cup type is china, steel, or glass
        elif self.__type == "china" or self.__type == "steel" or self.__type == "glass":
            #these materials will be able to hold any drink, hot or cold
            self.__drinkswork = "Any drinks, hot or cold(such as coffee, soda, milk) will work with this type of cup."
            return self.__drinkswork
        #if the type initially is not one of the listed, then print an error
        else:
            print("Error. Not a valid size. Size can only be small, medium, or large.")
            

#define the main function
def main():
    
    #here we are building our own cup with the size as large and the type as glass. If we run this in terminal, we can use any of the methods on it
    #essentially here the program is calling the class Cup and then setting up the variable own_cup(in terminal we have to first import the class from module MyOwnClass)
    #then in terminal, we can apply any of the methods to own_cup if we want, for instance we could run own_cup.cup_volume() and it would give 16oz
    own_cup = Cup("large", "glass")

    #here we are again building our cup this time as a variable x with medium sie and plastic type
    x = Cup("medium", "plastic")
    #printing it to show in Visual Studio Code
    print(x)
    #we are calling the class variable has_opening, which should print True since all cups(no matter size or type have an openeing)
    y = x.has_opening
    print(y)
    #here we can calling the get_type method on the original cup we built(x)
    #this method will print "plastic" as we did not create a new type so it should return the original
    y = x.get_type()
    print(y)
    #here we can calling the get_size method on the original cup we built(x)
    #this method will print "medium" as we did not create a new size so it should return the original
    y = x.get_size()
    print(y)
    #this is calling the volume of the cup we built(x)
    #the original cup size we set it as was "medium" so it should return 12oz for volume
    y = x.cup_volume()
    print(y)
    #this is calling the which drinks work method for the cup we built(x)
    #the original cup type we set was plastic so it should say no hot drinks will work with this cup
    y = x.which_drinkswork()
    print(y)


    #here we are again building our cup this time as a variable make_cup with small sie and china type
    make_cup = Cup("small", "china")
    #now we are implementing the set_size method and changing our "small" size to now "large"
    make_cup.set_size("large")
    #similarly to size, we are using the set_type method and changing the type from "china" to "wood"
    make_cup.set_type("wood")
    #we are calling the get_size method which should return the new set_size instead of the original since the method adjusts to the change
    y = make_cup.get_size()
    print(y)
    #we are calling the get_type method which should return the new set_type instead of the original since the method adjusts to the change
    y = make_cup.get_type()
    print(y)
    #with our new built cup, we are now finding the volume of it using the cup_volume method
    #this will return the volume of the new set_size since the method adjusts to the change
    y = make_cup.cup_volume()
    print(y)
    #with our new built cup, we are now finding which drinks work with the type using the which_drinkswork method
    #this will return the statement of which drinks will work of the new set_type since the method adjusts to the change(it would say no hot drinks work)
    y = make_cup.which_drinkswork()
    print(y)
    

if __name__ == "__main__":
    main()
