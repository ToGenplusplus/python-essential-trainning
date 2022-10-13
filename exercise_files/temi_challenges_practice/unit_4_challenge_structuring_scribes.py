from codecs import namereplace_errors
import os
import time
import math
import names
from termcolor import colored

#Objective:
# - create a data structure that holds information about each scribe (starting positions, directions, names, movements)
# - write a function that creates and moves scribes based on this data structure
# 



class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

class TerminalScribeStorm:

    def __init__(self, number_of_scribes) -> None:
        self.scribes_definitions: list[dict] 
        self.scribe_number = number_of_scribes
        self.__generateScribeDefinitions()
        pass

    def __generateScribeDefinitions(self):
        self.scribes_definitions = [{'name':f"Scribe-{names.get_first_name()}", 'direction': round(180/i), 'movements':[('forward','5')]} for i in range(1, self.scribe_number + 1)]

    def __generateScribe(self, direction: int):
        aScribe = TerminalScribe(Canvas(30,30))
        aScribe.setDegrees(direction)
        return aScribe

    def __printScribeInfo(self, scribeDefinition: dict):
        name = scribeDefinition["name"]
        direction = scribeDefinition["direction"]
        movements = scribeDefinition["movements"]
        print(colored(f"Scribe name: {name}","green",attrs=["bold"]))
        print(colored(f"Scribe direction: {direction}","green",attrs=["bold"]))
        print(colored(f"Scribe movements: {movements}","green",attrs=["bold"]))

    def __activateScribeMovements(self, scribe: TerminalScribe, movementData: list[tuple]):
        for movement in movementData:
            match movement[0]:
                case 'forward':
                    for _ in range(int(movement[1])):
                        scribe.forward()
                case 'up':
                    for _ in range(int(movement[1])):
                        scribe.up()
                case 'down':
                    for _ in range(int(movement[1])):
                        scribe.down()
                case 'right':
                    for _ in range(int(movement[1])):
                        scribe.right()
                case 'left':
                    for _ in range(int(movement[1])):
                        scribe.left()

    def stormTheTerminal(self):
        for definition in self.scribes_definitions:
            scribeFromDefinition = self.__generateScribe(definition.get("direction",0))
            self.__printScribeInfo(definition)
            self.__activateScribeMovements(scribeFromDefinition, definition["movements"])
            print("\n")


# canvas = Canvas(30, 30)
# scribe = TerminalScribe(canvas)
# scribe.setDegrees(135)
# for i in range(30):
#     scribe.forward()

def main():
    scribeStorm = TerminalScribeStorm(2)
    scribeStorm.stormTheTerminal()

if __name__ == '__main__':
    main()
