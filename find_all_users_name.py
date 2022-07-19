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
    arr1=[]
    for i in data["messages"] :
        arr.append(i.get('actor'))
        arr.append(i.get('from'))
    for k in arr :
        if k!=0:
            if k not in arr1 :
                arr1.append(k) 
    return arr1
    
print(find_all_users_name(read_data("data/result.json")))
