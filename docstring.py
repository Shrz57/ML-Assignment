from typing import List, Dict,Optional
def convert_list_to_dict(dict_a:Dict ,list_keys:List,list_values:List)->int:
    """_To Convert List to Dictionary

    Args:
        dict_a (Dict): _description_
        list_keys (List): _description_
        list_values (List): _description_

    Returns:
        int: _description_
    """    
    for idx, items in enumerate(list_keys):
        dict_a[items]=list_values[idx]


