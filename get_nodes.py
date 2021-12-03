import requests

def get_nodes(country_code="IT"):
    """
    :string: country_code
    Returns all the nodes for a given country, with each provider name.
    
    """
    url = "https://bitnodes.io/api/v1/snapshots/latest"

    COUNTRY_CODE = country_code.upper()

    nodes = requests.get(url).json()

    list_all_nodes = list(nodes["nodes"].values())

    for node in list_all_nodes:
        if node[7] == COUNTRY_CODE:
            print(f"Provider Name: {node[12]}")
            print(f"City: {node[6]}")
            
if __name__ == "__main__":
    get_nodes()
    