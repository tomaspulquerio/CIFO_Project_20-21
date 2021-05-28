from numpy.core.shape_base import block
from setup import Number_of_Digits as Number_of_Digits
import setup as v
import random
import numpy as np
import random
import operator
from past.builtins import range


class Individual(object):
    

    def __init__(self):
        self.values = np.zeros((Number_of_Digits, Number_of_Digits))
        self.fitness = None
        return

    def update_fitness(self):

        #Fitness was designed in a way where it would be evaluated in two diferent ways and then sumarized into the final fitness
        #First we will do the line_counter, where we will confirm the number of diferent number for each line, for each one we will add
        #to line_counter (1/9)/9, if there is no duplicate numbers in any line line counter will assume the value 1 ((1/9)/9)*81=1
        #after confirming the lines we will see if each block of 3x3 also has no duplicate number, following the same aproach where, if 
        #all numbers are unique in all blocks the block_counter will be 1 
        #in the end to calculate the fitness we just need to multiply with each other, wich will translate into a number between 0 and 1 
        #where 1 is a solution for the sudoku
        line_counter = np.zeros(Number_of_Digits)
        block_counter = np.zeros(Number_of_Digits)
        column_sum = 0
        block_sum = 0
        
        

        self.values = self.values.astype(int)
        for j in range(0, Number_of_Digits):
            for i in range(0, Number_of_Digits):
                line_counter[self.values[i][j] - 1] += 1

            
            for k in range(len(line_counter)):
                if line_counter[k] == 1:
                    column_sum += (1/Number_of_Digits)/Number_of_Digits
            line_counter = np.zeros(Number_of_Digits)

        
        for i in range(0, Number_of_Digits, 3):
            for j in range(0, Number_of_Digits, 3):
                block_counter[self.values[i][j] - 1] += 1
                block_counter[self.values[i][j + 1] - 1] += 1
                block_counter[self.values[i][j + 2] - 1] += 1

                block_counter[self.values[i + 1][j] - 1] += 1
                block_counter[self.values[i + 1][j + 1] - 1] += 1
                block_counter[self.values[i + 1][j + 2] - 1] += 1

                block_counter[self.values[i + 2][j] - 1] += 1
                block_counter[self.values[i + 2][j + 1] - 1] += 1
                block_counter[self.values[i + 2][j + 2] - 1] += 1

                for k in range(len(block_counter)):
                    if block_counter[k] == 1:
                        block_sum += (1/Number_of_Digits)/Number_of_Digits
                block_counter = np.zeros(Number_of_Digits)
        
        # Calculate the final fitness.
        
        if int(column_sum) == 1 and int(block_sum) == 1:
            fitness = 1.0
        else:
            fitness = column_sum * block_sum

        self.fitness = fitness
        return