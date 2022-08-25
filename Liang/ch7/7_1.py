#Anson Allseitz
#(The  Rectangle class) Following the example of the Circle class in Section 7.2, design a class named 
#Rectangle to represent a rectangle. The class contains:

#Two data fields named width and height
#A constructor that creates a rectangle with the specified width and height. The default values are 1 and 2 
#for the width and height respectively
#a method named getarea() that returns the area of the rectangle 
#a method named getPerimeter that returns the perimeter:


class Rectangle:
    #Construct a rectangle object
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height 

    def getArea(self):
        return self.width * self.height 

    def getPerimeter(self): 
        return (self.width *2) + (self.height *2)

def main(): 

    myRectangle = Rectangle()
    print("The area of the rectangle is", myRectangle.getArea())

    print("The width of the rectangle is now: ", myRectangle.width)
    print("The height of the rectangle is now: ", myRectangle.height)

    
main() 
    