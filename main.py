from NeuralNetwork import *
from Snake import *
import pygame
from pygame.locals import QUIT
import math
from GeneticAlgorithm import *


#---------------------------------------------------------------------
# Initialise screen
pygame.init()
screen_size = (600, 600)
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('Snake_Genetic_Algorithm')
canvas = pygame.Surface(screen_size)


geneticAlg = GeneticAlgorithm(screen, canvas, screen_size)



# Event loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    geneticAlg.Cycle()

    



