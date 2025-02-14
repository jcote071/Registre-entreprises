import requests
import pandas as pd
import math
import os
import pickle
from pydantic import validate_call

@validate_call
def import_data_from_dq_api(url:str) -> pd.DataFrame:
    '''
    
    '''
    try:
        response = requests.get(url)
    except Exception as e:
        print("Error:{e}")

    nb_records = response.json()['result']['total']

    nb_loop_iterations = math.ceil(nb_records/100)
    
    df = d.DataFrame(
    response.json()['result']['records']
    )


    for i in range(nb_loop_iterations):
        try:
            print(response.json()['result']['_links']['next'])
            next_response = ''.join([
                'https://www.donneesquebec.ca/recherche/',
                response.json()['result']['_links']['next']
            ])
            response = requests.get(
                next_response
            )
            next_df = pd.DataFrame(
                response.json()['result']['records']
            )
            df = pd.concat([df,next_df])
            continue
        except Exception as e:
            print(f"Error:{e}")
            break
            
    return df

@validate_call
def pickle_to_temp(obj:object,filename:str)-> None:
    '''
    
    '''
    file_path = os.path.join(
        ".",
        "input",
        "temp",
        f"{filename}.pkl"
    )
    
    pickle.dump(obj=obj,file=filename)
    