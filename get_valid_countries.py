import requests

def get_countries():
    """
    Returns a list of valid countries
    """
    valid_countries = []
    url = "https://bitnodes.io/api/v1/snapshots/latest"
    
    try:
        nodes = requests.get(url).json()
    except ConnectionError():
        print("[!] Connection Error")
        
    list_all_nodes = list(nodes["nodes"].values())
    for node in list_all_nodes:
        if node[7] is not None:
            valid_countries.append(node[7])
    
    valid_countries = set(valid_countries)
    print(valid_countries)
    return valid_countries

if __name__ == "__main__":
    get_countries()
    