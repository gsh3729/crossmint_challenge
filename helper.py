from megaverse import AstralObject
import requests
from constants import *

# func to get goal map information
def get_goal_data():
    get_request = lambda : requests.get(Constants.MAP_URL)
    astral = AstralObject()
    
    try:
        goal_data = astral.callApi(get_request)
    except Exception as e:
        print(f"Exception error in getting goal data: {e}")

    if goal_data is not None:
        return goal_data.json()
    else:
        print("Error in getting response from goal api")
    return None