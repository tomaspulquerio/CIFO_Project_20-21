import numpy as np
import pandas as pd
import setup as v


dict = {'Selection':[v.Selection],
        'Mutation': [v.Crossover],
        'Crossover':[v.Crossover],
        'Run':[v.d],
        'Generation':[0],
        'Fitness':[0],
        }
 

df_cifo = pd.DataFrame(dict)

def dataframe_update(dict_temp):
    df1 = pd.DataFrame(dict_temp)
    global df_cifo
    df_cifo = df_cifo.append(df1, ignore_index=True)
    return
    
def save_dataframe():
    
    df_cifo.to_csv("cifo_results_singlepoint_tour_3mutations.csv")
    df_confirmation = pd.read_csv("cifo_results_singlepoint_tour_3mutations.csv")
    print(df_confirmation.head(5))
    return

def create_dataframe():
    dict = {'Selection':[v.Selection],
        'Mutation': [v.Crossover],
        'Crossover':[v.Crossover],
        'Run':[v.d],
        'Generation':[0],
        'Fitness':[0],
        }
    
     # creating a dataframe from list
    df_cifo = pd.DataFrame(dict)
    return
    