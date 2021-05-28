from numpy.core.shape_base import block
from setup import Number_of_Digits, Number_of_individuals
import setup as v
import random
import numpy as np
import random
import operator
from past.builtins import range
import Individual as Individual

class Population(object):
    

    def __init__(self):
        self.Individuals = []
        return

    def seed(self, Number_of_individuals, given):
        self.Individuals = []

        
        helper = Individual.Individual()
        helper.values = [[[] for j in range(0, Number_of_Digits)] for i in range(0, Number_of_Digits)]
        for row in range(0, Number_of_Digits):
            for column in range(0, Number_of_Digits):
                for value in range(1, 10):
                    if ((given.values[row][column] == 0) and not (given.is_column_duplicate(column, value) or given.is_block_duplicate(row, column, value) or given.is_row_duplicate(row, value))):
                        
                        helper.values[row][column].append(value)
                    elif given.values[row][column] != 0:
                       
                        helper.values[row][column].append(given.values[row][column])
                        break

        # Seed a new population.
        for p in range(0, Number_of_individuals):
            g = Individual.Individual()
            for i in range(0, Number_of_Digits):  
                row = np.zeros(Number_of_Digits)

                
                for j in range(0, Number_of_Digits):  

                   
                    if given.values[i][j] != 0:
                        row[j] = given.values[i][j]
                    
                    elif given.values[i][j] == 0:
                        row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j]) - 1)]

                
                ii = 0
                while len(list(set(row))) != Number_of_Digits:
                    ii += 1
                    if ii > 500000:
                        return 0
                    for j in range(0, Number_of_Digits):
                        if given.values[i][j] == 0:
                            row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j]) - 1)]

                g.values[i] = row
            
            self.Individuals.append(g)
        
        self.update_fitness()

        

        return 1

    def update_fitness(self):
        
        for Individual in self.Individuals:

            Individual.update_fitness()
        return

    def sort(self):
        
        
        self.Individuals = sorted(self.Individuals, key=operator.attrgetter('fitness'))
        return
        

