import json
import pickle


def read_pickle(pkl_path):
    '''
    Loading a Pickle file.

    Parameters
    ----------
    pkl_path : str
        Absolute path to the .pkl file.
        e.g, /mnt/project/summary.pickle

    '''
    with open(pkl_path, 'rb') as handle:
        pickle_dict = pickle.load(handle)
        
    return pickle_dict


def read_json(json_path):
    '''
    Loading a json file.

    Parameters
    ----------
    json_path : str
        Absolute path to the json file.
        e.g, /mnt/project/summary.json

    '''
    with open(json_path, 'rb') as handle:
        parsed_json = json.load(handle)
        
    return parsed_json


def write_pickle(pkl_path, my_dict):
    '''
    Writing to Pickle file

    Parameters
    ----------
    pkl_path : str
        Absolute path to  .pkl file.
        e.g, /mnt/project/summary.pickle
    my_dict : Dictionary (!?...)

    '''
    with open(pkl_path, 'wb') as handle:
        pickle.dump(my_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    return None


def write_json(json_path, config):
    '''
    Loading a json file.

    Parameters
    ----------
    json_path : str
        Absolute path to the json file.
        e.g, /mnt/project/summary.json
    config : Dictionary (!?...)

    '''
    
    with open(json_path, 'w') as handle:
        json.dump(config, handle, indent = 4)
        
    return None