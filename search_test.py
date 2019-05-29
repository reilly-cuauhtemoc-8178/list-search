#Search a list of lists for 
import requests

c_ids = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json")

lol = [
    ['a','b','c'],
    ['a','b','c'],
    ['c','d','e'],
    ['b','c','d']
]

def search_list(ltos):
    """
    Take list of lists and count elements in each one.

    Parameters:
    -----------
    ltos : list
        list of lists

    Returns: tuple(dict, int)
 
    """
    list_dict = dict()
    for sublist in ltos:
        for item in sublist:
            if list_dict.get(item, None) is None:
                list_dict[item] = 1
            else:
                list_dict[item] += 1
    return list_dict, len(ltos)

print(search_list(lol))