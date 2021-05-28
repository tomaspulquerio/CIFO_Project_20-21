from setup import Number_of_Digits
import setup as v
import random
import numpy as np
import random
import operator
from past.builtins import range
import Individual as c


class Crossover(object):
    
    
    def __init__(self):
        return
    
        

class SinglePointCrossover(object):

    def __init__(self):
        return

    def crossover(self, p1, p2, crossover_rate):

         child1 = c.Individual()
         child2 = c.Individual()

         test_rate = random.uniform(0, 2)
         while (test_rate > 1):  
             test_rate = random.uniform(0, 2)
        
         # Perform crossover.
         if (test_rate < crossover_rate):
            
            co_point = random.randint(1, len(p1.values)-2)

            for i in range(len(p1.values)):

                child1.values[i], child2.values[i] = self.no_duplicate_crossover(p1.values[i], p2.values[i], co_point)
            
            return child1, child2

    def no_duplicate_crossover(self, row_parent1, row_parent2, co_point):

        row_child1 = np.zeros(Number_of_Digits)
        row_child2 = np.zeros(Number_of_Digits)
        
        for i in range(len(row_parent1)):

            if i >= co_point:

                if (row_parent2[i] in row_child1):

                    row_child1[i] = row_parent1[i]
                else:

                    row_child1[i] = row_parent2[i]


                if (row_parent1[i] in row_child2):

                    row_child2[i] = row_parent2[i]
                else:

                    row_child2[i] = row_parent1[i]
                
            else:    
                
                row_child1[i] = row_parent1[i]
                row_child2[i] = row_parent2[i]

        return row_child1, row_child2

                    
                
               







class CycleCrossover(object):

    def __init__(self):
        return

    def crossover(self, p1, p2, crossover_rate):
          
        
        child1 = c.Individual()
        child2 = c.Individual()

        
        child1.values = np.copy(p1.values)
        child2.values = np.copy(p2.values)

        r = random.uniform(0, 1.1)
        while (r > 1):  
            r = random.uniform(0, 1.1)

        
        if (r < crossover_rate):
            
            cp1 = random.randint(0, 8)
            cp2 = random.randint(1, 9)
            while (cp1 == cp2):
                cp1 = random.randint(0, 8)
                cp2 = random.randint(1, 9)

            if (cp1 > cp2):
                temp = cp1
                cp1 = cp2
                cp2 = temp

            for i in range(cp1, cp2):
                child1.values[i], child2.values[i] = self.crossover_rows(child1.values[i], child2.values[i])

        return child1, child2

    def crossover_rows(self, row1, row2):
        child_row1 = np.zeros(Number_of_Digits)
        child_row2 = np.zeros(Number_of_Digits)

        remaining = range(1, Number_of_Digits + 1)
        cycle = 0

        while ((0 in child_row1) and (0 in child_row2)):  
            if (cycle % 2 == 0):  
                
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row1[index]
                child_row2[index] = row2[index]
                next = row2[index]

                while (next != start):  
                    index = self.find_value(row1, next)
                    child_row1[index] = row1[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row2[index]
                    next = row2[index]

                cycle += 1

            else:  
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row2[index]
                child_row2[index] = row1[index]
                next = row2[index]

                while (next != start):  
                    index = self.find_value(row1, next)
                    child_row1[index] = row2[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row1[index]
                    next = row2[index]

                cycle += 1

        return child_row1, child_row2

    def find_unused(self, row_parent, remaining):
        for i in range(0, len(row_parent)):
            if (row_parent[i] in remaining):
                return i

    def find_value(self, row_parent, value):
        for i in range(0, len(row_parent)):
            if (row_parent[i] == value):
                return i
