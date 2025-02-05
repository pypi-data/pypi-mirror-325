from digiwise_search_tac import init
import csv
import os

def search_list(path):
    s=init()
    list=read_csv(path)
    my_dict={}
    for item in list :
        
        my_dict[item]=s(item)
    return my_dict
    
    
def read_csv(pathcsv:str):
    with open(pathcsv, mode='r', encoding='utf-8') as file:
        line=file.read().splitlines()
    return line
 
def save_csv(dictionary: dict, file_path: str):
    """
    Saves a dictionary to a CSV file with 'key,value' format.
 
    :param dictionary: The dictionary to save
    :param file_path: Path to the output CSV file
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in dictionary.items():
            writer.writerow([key, value])
 
def batch_search(path_input,path_output=None):
    if path_output is None:
        path_output=path_input.replace('.csv','_output.csv')
    if os.path.exists(path_input):
        save_csv(search_list(path_input),path_output)
    else:
        raise FileNotFoundError(f"Erreur: le fichier '{path_input}' n'existe pas.")
