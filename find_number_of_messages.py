import json

from numpy import s_
from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    data = read_data("result.json")
    
    return len(data['messages'])
# print(find_number_of_messages('result.json'))