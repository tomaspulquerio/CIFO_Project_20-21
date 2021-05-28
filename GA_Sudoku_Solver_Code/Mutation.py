
import numpy as np
import random
import operator
import setup as v
from past.builtins import range

class Mutation(object):
    
    
    def __init__(self):
        return
    
    
###############################################################################################
def swap_mutation(self, mutation_rate, given):
   

    r = random.uniform(0, 1.1)
    while r > 1:  
        r = random.uniform(0, 1.1)

    success = False
    if r < mutation_rate:  
        while not success:
            row1 = random.randint(0, 8)
            row2 = random.randint(0, 8)
            

            from_column = random.randint(0, 8)
            to_column = random.randint(0, 8)
            while from_column == to_column:
                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)

                
            if given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0:
                
                if not given.is_column_duplicate(to_column, self.values[row1][from_column]) and not given.is_column_duplicate(from_column, self.values[row2][to_column]) and not given.is_block_duplicate(row2, to_column, self.values[row1][from_column]) and not given.is_block_duplicate(row1, from_column, self.values[row2][to_column]):
                    
                    temp = self.values[row2][to_column]
                    self.values[row2][to_column] = self.values[row1][from_column]
                    self.values[row1][from_column] = temp
                    success = True

    return success

###############################################################################################
def inversion_mutation(self, mutation_rate, given):

    r = random.uniform(0, 1.1)
    while r > 1:  
        r = random.uniform(0, 1.1)

    success = False
    if r < mutation_rate:  
        while not success:
            row1 = random.randint(0, 8)
            row2 = random.randint(0, 8)
            

            from_column = random.randint(0, 8)
            to_column = random.randint(0, 8)
            while from_column == to_column:
                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)

               
            if given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0:
            
                if not given.is_column_duplicate(to_column, self.values[row1][from_column]) and not given.is_column_duplicate(from_column, self.values[row2][to_column]) and not given.is_block_duplicate(row2, to_column, self.values[row1][from_column]) and not given.is_block_duplicate(row1, from_column, self.values[row2][to_column]):
                    
                    reversed(self.values[row1:row2][from_column:to_column])
                    
                    success = True
    
    return True

###############################################################################################
def scramble_mutation(self, mutation_rate, given):

    r = random.uniform(0, 1.1)
    while r > 1:  
        r = random.uniform(0, 1.1)

        success = False
        if r < mutation_rate:  
            while not success:
                row1 = random.randint(0, 8)
                row2 = random.randint(0, 8)
                

                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)
                while from_column == to_column:
                    from_column = random.randint(0, 8)
                    to_column = random.randint(0, 8)

                    
                if given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0:
                    
                    if not given.is_column_duplicate(to_column, self.values[row1][from_column]) and not given.is_column_duplicate(from_column, self.values[row2][to_column]) and not given.is_block_duplicate(row2, to_column, self.values[row1][from_column]) and not given.is_block_duplicate(row1, from_column, self.values[row2][to_column]):
                        
                        random.shuffle(self.values[row1:row2][from_column:to_column])
                        
                        
                        success = True
                        
    
    return True
###############################################################################################