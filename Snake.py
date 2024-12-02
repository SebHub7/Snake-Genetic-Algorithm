from EnumDirection import *
import random
import math
import pygame

class Snake:


    def __init__(self, gridDimension):
        self.gridDimension = gridDimension
        self.body = [[0, 0, None]] #x, y, direction
        self.fruitPosition = [0, 0]
        self.timeAlive = 0
        self.fruitsEaten = 0
        self.alive = True
        self.timeToLive = 0

        self.reset()

    
    def move(self, direction):

        #prevent snake to go back on himself
        if self.body[0][2] == Direction.N and direction != Direction.S:
            self.body[0][2] = direction

        if self.body[0][2] == Direction.S and direction != Direction.N:
            self.body[0][2] = direction

        if self.body[0][2] == Direction.E and direction != Direction.W:
            self.body[0][2] = direction

        if self.body[0][2] == Direction.W and direction != Direction.E:
            self.body[0][2] = direction



        #moving entire body
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
            self.body[i][2] = self.body[i-1][2]

  

        if self.body[0][2] == Direction.N:
            self.body[0][1] += 1

        if self.body[0][2] == Direction.S:
            self.body[0][1] -= 1

        if self.body[0][2] == Direction.W:
            self.body[0][0] -= 1

        if self.body[0][2] == Direction.E:
            self.body[0][0] += 1

        self.timeAlive += 1
        self.timeToLive -= 1

        if self.timeToLive <= 0:
            self.alive = False



    def collisions(self):
        headX = self.body[0][0]
        headY = self.body[0][1]

        #collision with walls
        if headX < 0 or headX > self.gridDimension:
            self.alive = False
            self.timeAlive  = math.floor(self.timeAlive / 10)

        if headY < 0 or headY > self.gridDimension:
            self.alive = False
            self.timeAlive = math.floor(self.timeAlive / 10)

        #collision with body
        #for i in range(1, len(self.body)):
        #    if headX == self.body[i][0] and headY == self.body[i][1]:
        #        self.alive = False




    def eat(self):

        if self.body[0][0] == self.fruitPosition[0] and self.body[0][1] == self.fruitPosition[1]:
            
            randomFruitX = math.floor(random.random() * (self.gridDimension - 0.01))
            randomFruitY = math.floor(random.random() * (self.gridDimension - 0.01))
            self.fruitPosition = [randomFruitX, randomFruitY]

            lastBlockX = self.body[len(self.body)-1][0]
            lastBlockY = self.body[len(self.body)-1][1]
            lastBlockDirection = self.body[len(self.body)-1][2]

            if lastBlockDirection == Direction.N:
                self.body.append([lastBlockX, lastBlockY-1, Direction.N])

            if lastBlockDirection == Direction.S:
                self.body.append([lastBlockX, lastBlockY+1, Direction.S])

            if lastBlockDirection == Direction.W:
                self.body.append([lastBlockX+1, lastBlockY, Direction.W])

            if lastBlockDirection == Direction.E:
                self.body.append([lastBlockX-1, lastBlockY, Direction.E])

            self.timeToLive += 100
            self.fruitsEaten += 1


    def pythagore(self, a, b):
        a1 = math.pow(a, 2)
        b1 = math.pow(b, 2)
        return math.sqrt(a1 + b1)


    def getData(self):
        distLeftWall = (self.body[0][0]) / self.gridDimension
        distRightWall = (self.gridDimension - self.body[0][0]) / self.gridDimension
        distTopWall = (self.body[0][1]) / self.gridDimension
        distDownWall = (self.gridDimension - self.body[0][1]) / self.gridDimension

        distLeftTopWall = self.pythagore(distLeftWall, distTopWall) / self.gridDimension
        distRightTopWall = self.pythagore(distRightWall, distTopWall) / self.gridDimension
        distRightDownWall = self.pythagore(distRightWall, distDownWall) / self.gridDimension
        distLeftDownWall = self.pythagore(distLeftWall, distDownWall) / self.gridDimension


        fruitLeft = 1 if self.fruitPosition[0] < self.body[0][0] else 0
        fruitRight = 1 if self.fruitPosition[0] > self.body[0][0] else 0
        fruitUp = 1 if self.fruitPosition[1] < self.body[0][1] else 0
        fruitDown = 1 if self.fruitPosition[1] > self.body[0][1] else 0

        



        data = [] #from snake pov, leftwall, rightwall, topwall, downwall
                #from snake pov, fruitLeft, fruitRight, fruitUp, fruitDown

        if self.body[0][2] == Direction.N:
            data = [distLeftWall, distRightWall, distTopWall, distDownWall]
            data += [fruitLeft, fruitRight, fruitUp, fruitDown]

        elif self.body[0][2] == Direction.S:
            data = [distRightWall, distLeftWall, distDownWall, distTopWall]
            data += [fruitRight, fruitLeft, fruitDown, fruitUp]

        elif self.body[0][2] == Direction.W:
            data = [distDownWall, distTopWall, distLeftWall, distRightWall]
            data += [fruitDown, fruitUp, fruitLeft, fruitRight]

        elif self.body[0][2] == Direction.E:
            data = [distTopWall, distDownWall, distRightWall, distLeftWall]
            data += [fruitUp, fruitDown, fruitRight, fruitLeft]


        return data



    def show(self, screen, canvas, screen_size):

        size_of_block = screen_size[0] / self.gridDimension
        #drawing fruit
        pygame.draw.rect(canvas,(255,0,0),(self.fruitPosition[0] * size_of_block, self.fruitPosition[1] * size_of_block, size_of_block, size_of_block))


        #drawing snake
        for i in range(len(self.body)):
            pygame.draw.rect(canvas,(0,255,0),(self.body[i][0] * size_of_block, self.body[i][1] * size_of_block, size_of_block, size_of_block))

        screen.blit(canvas,(0,0))



    def reset(self):
        self.timeAlive = 0
        self.fruitsEaten = 0
        self.alive = True
        self.fruitPosition = [0, 0, Direction(math.floor(random.random() * 3.99))]
        self.body = [[self.gridDimension/2, self.gridDimension/2, None]]
        self.timeToLive = 200
        
        #set random direction
        randomDirection = math.floor(random.random() * 3.99)
        self.body[0][2] = Direction(randomDirection)

        #set random fruit position
        randomFruitX = math.floor(random.random() * (self.gridDimension - 0.01))
        randomFruitY = math.floor(random.random() * (self.gridDimension - 0.01))
        self.fruitPosition = [randomFruitX, randomFruitY]

        #set random snake head position
        randomX = math.floor(random.random() * (self.gridDimension - 0.01))
        randomY = math.floor(random.random() * (self.gridDimension - 0.01))
        #self.body[0][0] = randomX
        #self.body[0][1] = randomY