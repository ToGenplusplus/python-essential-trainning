# the objective of this challenge is to draw a square on the terminal using the lessons learned in unit 2.
# Ex: given value 5, produce a square that is 5 units wide and 5 units tall 
# * * * 
# *   *              
#       
# Ex: given unit 1, just produce []
# Ex: given a negative unit value, print invalid value of unit and exit

# Draw Square class, with one class variable unit
# going to have a draw method 
# going to have a draw top/bottom square method
# going to have a draw sides of square method

import sys

class DrawSquare:
    def __init__(self, unit):
        if type(unit is not int) or unit < 1:
            print("Invalid unit value, expecting int >= 1")
            sys.exit(1)
        self.unit = unit

    def Draw(self):
        if (self.unit == 1):
            print("Haha clever a 1 unit square. Here you go: []")
        else:
            self.DrawSquareWithSpecifiedUnitSize()

    def DrawSquareWithSpecifiedUnitSize(self):
        self.DrawBase()
        self.DrawSides()
        self.DrawBase()

    def DrawBase(self):
        base = "* " * self.unit
        print(base)

    def DrawSides(self):
        # conditions for the sides
        # if unit = 2, there will be no sides drawn
        # if unit >= 3: 
        #   the number of spaces between the two sides is = (unit * 2) - 3
        #   number of * vertical = unit - 2
        if (self.unit >= 3):
            num_spaces_between_sides = (self.unit * 2) - 3
            num_vertical_hashes = self.unit - 2

            side = "*" + "" * num_spaces_between_sides + "*"
            for i in range(num_vertical_hashes):
                print(side)