import operator
from operator import attrgetter
import random 
import numpy as np
import setup as v



class Selection(object):
   

    def __init__(self):
        return
    
    

    def Fps(self, Individuals):
        
       
        total_fitness = sum([i.fitness for i in Individuals])
        
        spin = random.uniform(0, total_fitness)
        position = 0
        
        for individual in Individuals:
            position += individual.fitness
            if position > spin:
                return individual
        

        

    def Rank(self, Individuals):
    
        Individuals.sort(key=attrgetter('fitness'), reverse=True)
        

        
        total = len(Individuals)
       
        spin = random.uniform(0, total)
        position = 0
        
        for count, individual in enumerate(Individuals):
            position += count + 1
            if position > spin:
                return individual


    def Tournament(self, Individuals):
        
       
        c1 = Individuals[random.randint(0, len(Individuals) - 1)]
        c2 = Individuals[random.randint(0, len(Individuals) - 1)]
        f1 = c1.fitness
        f2 = c2.fitness

        
        if (f1 > f2):
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1



        
        
        selection_rate = v.selection_rate
        r = random.uniform(0, 1.1)
        while (r > 1):  
            r = random.uniform(0, 1.1)
        if (r < selection_rate):
            return fittest
        else:
            return weakest
    