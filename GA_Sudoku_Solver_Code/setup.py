import random
import pandas as pd
import time
import json
import numpy as np
from tkinter import *
from tkinter.ttk import *
import setup as v

from numpy.core.records import array

#import the file that contains all of our sudokus, with diferent dificulties
file = "Sudoku_database.json"
with open(file) as f:
        data = json.load(f)

Batch_run = True

easy = data['Easy']
medium = data['Medium']
hard = data['Hard']
expert = data['Expert']

#Chose the dificulty you want 
dificulty = easy

# Maximization or Minimization
option = "maximization"
# Selection Method to be used #Fps #Rank #Tournament
Selection = "Rank"
# Mutation Method to be used  #inversion_mutation #swap_mutation #scramble_mutation
Mutation = "scramble_mutation"
# Crossover Method to be used #SinglePointCrossover #CycleCrossover
Crossover = "SinglePointCrossover"
# Number of digits in the Sudoku, Standart = 9 
Number_of_Digits =9
# Number of Individuals (i.e. population size).
Number_of_individuals = 700
# Number of elites.
Number_of_elites = int(0.05 * Number_of_individuals)  
# Number of generations.
Number_of_generations = 500 
# Number of mutations.
Number_of_mutations = 1
# Mutation parameters.      
mutation_rate = 0.09
#Selection parameters
selection_rate = 0.75
#Crossover parameters
crossover_rate = 0.8

#Re-seed the population if 100 generations have passed with the fittest two Individuals always having the same fitness.
re_seed = 50

loop = 0

array = []

a = 0
b = 0 
c = 0 
d = 0

Selection_array = [ "Tournament"]
Mutation_array = ["inversion_mutation", "swap_mutation" ,"scramble_mutation"]
Crossover_array = ["CycleCrossover"]
#,"SinglePointCrossover"


dict = {'Selection':[v.Selection],
        'Mutation': [v.Crossover],
        'Crossover':[v.Crossover],
        'Run':[d],
        'Generation':[0],
        'Fitness':[0],
        }
 
# creating a dataframe from list
df = pd.DataFrame(dict)
