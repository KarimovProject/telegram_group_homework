import json
from read_data import read_data
def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    message = data['messages']
    return len(message)
path  = 'data/result.json'
data = read_data(path)