import random
import math
from EnumDirection import *
import numpy as np


class NeuralNetwork:
    
    def __init__(self, tab_neurones_per_layer):
        self.nb_layer = len(tab_neurones_per_layer)
        self.tab_neurones_per_layer = tab_neurones_per_layer
        self.layers = []


        for h in range(1, self.nb_layer):
            self.layers.append([])

            for n in range(self.tab_neurones_per_layer[h]):
                self.layers[h-1].append([])

                for i in range(self.tab_neurones_per_layer[h-1] + 1):
                    randomWeight = -1 + random.random() * 2
                    self.layers[h-1][n].append(randomWeight)
 
    

    def propagation(self, data):
        
        layer_output = []
        
        for h in range(1, self.nb_layer):
            layer_output = []

            for n in range(self.tab_neurones_per_layer[h]):
                out = 0

                for i in range(self.tab_neurones_per_layer[h-1]):
                    out += data[i] * self.layers[h-1][n][i]

                #adding bias
                out += self.layers[h-1][n][self.tab_neurones_per_layer[h-1]]

                out = self.sigmoid(out)
                layer_output.append(out)
            
            data = layer_output
        


        #getting direction predicted
        maximum = max(layer_output)
        index = layer_output.index(maximum)
        directionChosen = Direction(index)

        return directionChosen


            
                
    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))



    def crossOver(self, neuralNet1, neuralNet2):

        for h in range(1, self.nb_layer):
            for n in range(self.tab_neurones_per_layer[h]):
                for i in range(self.tab_neurones_per_layer[h-1] + 1):

                    if random.random() > 0.5:
                        self.layers[h-1][n][i] = neuralNet1.layers[h-1][n][i]
                    else:
                        self.layers[h-1][n][i] = neuralNet2.layers[h-1][n][i]



    def mutate(self, mutationRate):

        for h in range(1, self.nb_layer):
            for n in range(self.tab_neurones_per_layer[h]):
                for i in range(self.tab_neurones_per_layer[h-1] + 1):

                    if random.random() < mutationRate:
                        newWeight = random.random()
                        self.layers[h-1][n][i] = newWeight


        

    


        





