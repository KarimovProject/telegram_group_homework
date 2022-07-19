from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    message = data['messages']
    for usr in message:
        users_id = usr.get('from_id')
        if users_id and users_id not in users_id:
            users_id.append(users_id)
        #users_id.remove('channel1474589327')
path = 'data/result.json'
data = read_data(path)
print(find_all_users_id(data))