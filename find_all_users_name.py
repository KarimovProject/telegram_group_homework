from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    arr=[]
    arr1 = []
    for i in data["messages"] :
        actor  = i.get('actor')
        if actor and actor not in arr:
            arr.append(actor)
        from_usr = i.get('from')
        if from_usr and from_usr not in from_usr:
            arr1.append(from_usr)
    return list(set(arr+arr1))
path = 'data/result.json'
data = read_data(path)
