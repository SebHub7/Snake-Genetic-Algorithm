import random
import math
from NeuralNetwork import *
from Game import *

class GeneticAlgorithm:

    def __init__(self, screen, canvas, screen_size):
        self.screen = screen
        self.canvas = canvas
        self.screen_size = screen_size

        self.population = 500
        self.generation = 1
        self.Game = Game(self.population)

        self.neurals_networks = []
        self.tab_neurones_per_layer = [8, 4]#input, layers, output


        for i in range(self.population):
            self.neurals_networks.append(NeuralNetwork(self.tab_neurones_per_layer))



    def createScoreArray(self, snakes):
        snakes_score = []

        for i in range(self.population):
            score = snakes[i].timeAlive + snakes[i].fruitsEaten * 300
            snakes_score.append(score)
        
        return snakes_score
        

    def createProbabilityArray(self, snakes_score):
        probability_array = []

        for i in range(self.population):
            for k in range(snakes_score[i]):
                probability_array.append(i)

        return probability_array

    
    def createNewPopulation(self, probability_array):
        new_neural_networks = []

        #creating childs
        for i in range(self.population):
            randomIndex1 = math.floor(random.random() * (len(probability_array) - 0.01))
            randomIndex2 = math.floor(random.random() * (len(probability_array) - 0.01))

            indexParent1 = probability_array[randomIndex1]
            indexParent2 = probability_array[randomIndex2]

            n1 = self.neurals_networks[indexParent1]
            n2 = self.neurals_networks[indexParent2]
            child = NeuralNetwork(self.tab_neurones_per_layer)
            child.crossOver(n1, n2)
            child.mutate(0.01)
            new_neural_networks.append(child)


        return new_neural_networks


    def Cycle(self):
        
        if not self.Game.Play(self.screen, self.canvas, self.screen_size, self.neurals_networks): #generation is dead

            snakes_score = self.createScoreArray(self.Game.snakes)
            probability_array = self.createProbabilityArray(snakes_score)
            self.neurals_networks = self.createNewPopulation(probability_array)
            self.Game.reset()

            self.generation += 1
            print("Generation: " + str(self.generation))





        
