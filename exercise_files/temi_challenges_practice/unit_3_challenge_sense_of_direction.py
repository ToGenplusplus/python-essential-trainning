import os
import time
import math
from termcolor import colored

# Objective for this challenge, add a direction attribute so the terminal knows which way it is pointing
# create a function called forward that moves the pointer in that direction.
# the pointer should be able to move in any direction between 0 and 180 degrees.

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas, direction):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]
        self.initialPos = [15,15]
        self.direction = direction
        self.destination = [0,1]

    def __setDestindationPoint(self):
        # convert the direction in degrees to radian
        # get the x coordinate = cos(rad)
        # get the y coordinate = sin(rad)
        rad = math.radians(self.direction)
        dest_x = round(math.sin(rad) * 15)
        dest_y = round(math.cos(rad) * 15)
        self.destination = [dest_x, dest_y]

        pass

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def forward(self):
        i = 0
        if not self.canvas.hitsWall(self.initialPos):
            self.draw(self.initialPos)
            pass

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)
 
canvas = Canvas(30, 30)

scribe = TerminalScribe(canvas)


