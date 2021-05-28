import numpy as np
import random
import pandas as pd
import operator
from past.builtins import range
import setup as v
import Selection as s
import Mutation as m
import Crossover as Crossover
import Individual as Individual
import Population as Population
import csv_saver as csv_saver



random.seed()

Number_of_Digits = v.Number_of_Digits 





    


class Fixed_grid(Individual.Individual):
    

    def __init__(self, values):
        self.values = values
        return

    def is_row_duplicate(self, row, value):
        
        for column in range(0, Number_of_Digits):
            if self.values[row][column] == value:
                return True
        return False

    def is_column_duplicate(self, column, value):
        
        for row in range(0, Number_of_Digits):
            if self.values[row][column] == value:
                return True
        return False

    def is_block_duplicate(self, row, column, value):
        
        i = 3 * (int(row / 3))
        j = 3 * (int(column / 3))

        if ((self.values[i][j] == value)
            or (self.values[i][j + 1] == value)
            or (self.values[i][j + 2] == value)
            or (self.values[i + 1][j] == value)
            or (self.values[i + 1][j + 1] == value)
            or (self.values[i + 1][j + 2] == value)
            or (self.values[i + 2][j] == value)
            or (self.values[i + 2][j + 1] == value)
            or (self.values[i + 2][j + 2] == value)):
            return True
        else:
            return False

    def make_index(self, v):
        if v <= 2:
            return 0
        elif v <= 5:
            return 3
        else:
            return 6

    def no_duplicates(self):
        for row in range(0, Number_of_Digits):
            for col in range(0, Number_of_Digits):
                if self.values[row][col] != 0:

                    cnt1 = list(self.values[row]).count(self.values[row][col])
                    cnt2 = list(self.values[:,col]).count(self.values[row][col])

                    block_values = [y[self.make_index(col):self.make_index(col)+3] for y in
                                    self.values[self.make_index(row):self.make_index(row)+3]]
                    block_values_ = [int(x) for y in block_values for x in y]
                    cnt3 = block_values_.count(self.values[row][col])

                    if cnt1 > 1 or cnt2 > 1 or cnt3 > 1:
                        return False
        return True


class Sudoku(object):
    

    def __init__(self):
        self.given = None
        return

   
    def load(self, p):
        
        self.given = Fixed_grid(p)
        return

    def solve(self):

        Number_of_individuals = v.Number_of_individuals # Number of Individuals (i.e. population size).
        Number_of_elites = v.Number_of_elites  # Number of elites.
        Number_of_generations = v.Number_of_generations # Number of generations.
        Number_of_mutations = v.Number_of_mutations # Number of mutations.
        crossover_rate = v.crossover_rate 
        selection_rate = v.selection_rate 
       

        
        
        mutation_rate = v.mutation_rate

        #See if there is duplicates
        if self.given.no_duplicates() == False:
            return (-1, 1)

        # Seed the population
        self.population = Population.Population()
        
        print("We are currently using :")
        print("Selection Method --> " + v.Selection)
        print("Mutation Method --> " + v.Mutation)
        print("Crossover Method --> " + v.Crossover)
        print("creating an initial population.")
        if self.population.seed(Number_of_individuals, self.given) ==  1:
            pass
        else:
            return (-1, 1)

        
        stale = 0
        for generation in range(0, Number_of_generations):

           
            
            best_fitness = 0.0
            
            
            for c in range(0, Number_of_individuals):
                fitness = self.population.Individuals[c].fitness
               
                
                if (fitness == 1):
                    print("Solution found at generation %d!" % generation)
                    return (generation, self.population.Individuals[c])
                if (fitness > best_fitness):
                    best_fitness = fitness
                    
            
            print("Generation:", generation, " Best fitness:", round(best_fitness, 15))

            #save the values for csv
            dict_temp = {'Selection':[v.Selection],
                    'Mutation': [v.Crossover],
                    'Crossover':[v.Crossover],
                    'Run':[v.d],
                    'Generation':[generation],
                    'Fitness':[best_fitness],
                    }
            
            csv_saver.dataframe_update(dict_temp)
            

            

            # Create next pop
            next_population = []

            # elitism
            self.population.sort()
               
            elites = []
            for e in range(0, Number_of_elites):
                elite = Individual.Individual()
                elite.values = np.copy(self.population.Individuals[e].values)
                elites.append(elite)

            ###SELECTION###
            for count in range(Number_of_elites, Number_of_individuals, 2):
                
                selection = s.Selection()
                if(v.Selection == "Tournament"):
                    parent1 = selection.Tournament(self.population.Individuals)
                    parent2 = selection.Tournament(self.population.Individuals)
                    
                if(v.Selection == "Fps"):
                    parent1 = selection.Fps(self.population.Individuals)
                    parent2 = selection.Fps(self.population.Individuals)

                if(v.Selection == "Rank"):
                    parent1 = selection.Rank(self.population.Individuals)
                    parent2 = selection.Rank(self.population.Individuals)

                

                ###CROSSOVER###
                if(v.Crossover=="CycleCrossover"):
                    cc = Crossover.CycleCrossover()
                elif(v.Crossover=="SinglePointCrossover"):
                    cc = Crossover.SinglePointCrossover()
                

                crossover_rate=v.crossover_rate
                child1, child2 = cc.crossover(parent1, parent2, crossover_rate)

                ###MUTATION###
                
                child1.update_fitness()
                old_fitness = child1.fitness
                success = False


                if(v.Mutation == "swap_mutation"):
                    success = m.swap_mutation(child1,mutation_rate, self.given)
               
                if(v.Mutation == "scramble_mutation"):
                    success = m.scramble_mutation(child1,mutation_rate, self.given)

                if(v.Mutation == "inversion_mutation"):
                    success = m.inversion_mutation(child1,mutation_rate, self.given)


                child1.update_fitness()
                if (success):
                    Number_of_mutations += 1
                    

                
                child2.update_fitness()
                old_fitness = child2.fitness

                success = False
                if(v.Mutation == "swap_mutation"):
                    success = m.swap_mutation(child2,mutation_rate, self.given)
                if(v.Mutation == "scramble_mutation"):
                    success = m.scramble_mutation(child2,mutation_rate, self.given)
                if(v.Mutation == "inversion_mutation"):
                    success = m.inversion_mutation(child2,mutation_rate, self.given)

                child2.update_fitness()
                if (success):
                    Number_of_mutations += 1
                    

                
                next_population.append(child1)
                next_population.append(child2)

            
            for e in range(0, Number_of_elites):
                next_population.append(elites[e])

            
            self.population.Individuals = next_population
            self.population.update_fitness()


            
            self.population.sort()
            if (self.population.Individuals[0].fitness != self.population.Individuals[1].fitness):
                stale = 0
            else:
                stale += 1
            
           
            
            if(stale >= v.re_seed / 2):
                mutation_rate = mutation_rate * 3
                v.mutation_rate = mutation_rate
            
            elif(stale >= v.re_seed / 3):
                mutation_rate = mutation_rate * 2
                v.mutation_rate = mutation_rate
            
            elif(stale >= v.re_seed / 4):
                mutation_rate = mutation_rate * 1.4
                v.mutation_rate = mutation_rate
            
            elif(stale >= v.re_seed / 5):
                mutation_rate = mutation_rate * 1.2
                v.mutation_rate = mutation_rate
            
            
            
                




            if (stale >= v.re_seed):
                print("The population has gone stale. Re-seeding...")
                self.population.seed(Number_of_individuals, self.given)
                stale = 0
                
                mutation_rate = v.mutation_rate

        print("No solution found.")
        return (-2, 1)