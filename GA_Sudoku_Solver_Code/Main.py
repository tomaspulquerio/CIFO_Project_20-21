
import random
import time
import json
import numpy as np
import pandas as pd
from numpy.core.records import array
import pandas as pd
from tkinter import *
from tkinter.ttk import *
import Solver as gss
import setup as v
random.seed(time.time())
import csv_saver as csv_saver


#select wich dificulty you want 
given = v.dificulty[random.randint(0,len(v.dificulty)-1)]
grid = np.array(list(given)).reshape((9,9)).astype(int)
#this is your sudoku empty grid, selected randomly from the ones in the selected dificulty
print(grid)



csv_saver.create_dataframe()
if v.Batch_run==True :

    for a in range(1):
        for b in range(3):
                for c in range(1):
                    for d in range(50):
                        #select wich dificulty you want 
                        given = v.dificulty[random.randint(0,len(v.dificulty)-1)]
                        grid = np.array(list(given)).reshape((9,9)).astype(int)
                        #this is your sudoku empty grid, selected randomly from the ones in the selected dificulty
                        print(grid)
                        v.a = a 
                        v.b = b
                        v.c = c 
                        v.d = d
                        v.Selection = v.Selection_array[a]
                        v.Mutation= v.Mutation_array[b]
                        v.Crossover = v.Crossover_array[c]
                        s = gss.Sudoku()
                        s.load(grid)
                        start_time = time.time()
                        generation, solution = s.solve()
                        v.loop+=1
                        
    print("Batch is complete")                 
    csv_saver.save_dataframe()





else:
    given = v.dificulty[random.randint(0,len(v.dificulty)-1)]
    grid = np.array(list(given)).reshape((9,9)).astype(int)
    #this is your sudoku empty grid, selected randomly from the ones in the selected dificulty
    print(grid)
    s = gss.Sudoku()
    s.load(grid)
    start_time = time.time()
    generation, solution = s.solve()


