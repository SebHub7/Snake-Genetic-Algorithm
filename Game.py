from Snake import *
import pygame

class Game:

    def __init__(self, population):
        self.dimension = 50
        self.population = population
        self.snakes = []
        self.snakesAlive = population

        for i in range(population):
            self.snakes.append(Snake(self.dimension))

    
    
    def reset(self):

        for i in range(self.population):
            self.snakes[i].reset()

        self.snakesAlive = self.population


    def Play(self, screen, canvas, screen_size, neurals_networks):

        canvas.fill((0,0,0))

        for i in range(self.population):

            if self.snakes[i].alive:
                data = self.snakes[i].getData()
                outputDirection = neurals_networks[i].propagation(data)
                self.snakes[i].move(outputDirection)
                self.snakes[i].collisions()
                self.snakes[i].eat()

                self.snakes[i].show(screen, canvas, screen_size)


                if self.snakes[i].alive == False:
                    self.snakesAlive -= 1

        pygame.display.update()
        pygame.time.delay(10)

        if self.snakesAlive <= 0:
            return False
        
        return True

