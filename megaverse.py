import requests
import json
import time
from constants import *

# AstralObject is the main class
# Cometh, Soloon, and Polyanet are child classes to the AstralObject
# AstralObject contains _callPostApi, _callDeleteApi (protected methods) which can be accessed by child classes
# Methods in parent class accept payload to send to the api
# Childclass methods builds the payload and sends the payload to the parent class for further processing

class AstralObject():
    def __callApi(self, api_func, max_retries=5): 
        # retry mechanism for too many requests (exponential increase in sleep time)
        retries = 0
        while retries < max_retries:
            response = api_func()

            if response.status_code == 200:
                # print(f"Matrix updated via API")
                return response 
            elif response.status_code == 429:
                # print("Too many requests. Retrying after backoff...")
                time.sleep(2 ** retries)  #exponential increase in sleep time
                retries += 1
            else:
                print(f"Error updating map via API: {response.content}")
                return  
        
        print("Max retries reached. Could not update map.")
        return None

    def _callPostApi(self, object_type, payload): 
        api_url = Constants.BASE_URL + object_type
        post_req = lambda: requests.post(api_url, data=payload, headers={'Content-Type': 'application/json'})
        self.callApi(post_req)
        return

    def _callDeleteApi(self, object_type, payload):
        api_url = Constants.BASE_URL + object_type
        delete_req = lambda: requests.delete(api_url, data=payload, headers={'Content-Type': 'application/json'})
        self.callApi(delete_req)
        return



class Cometh(AstralObject):
    def __init__(self, direction="LEFT"):
        super().__init__()
        self.direction = direction
    
    def callPostApi(self, row, column):
        payload = {"candidateId": Constants.CANDIDATE_ID, "row": row, "column": column, "direction": self.direction}
        json_payload = json.dumps(payload)
        super()._callPostApi(Api_Astral_Type.COMETH.value, json_payload)
        return
    
    def callDeleteApi(self, row, column):
        payload = {"candidateId": Constants.CANDIDATE_ID, "row": row, "column": column}
        json_payload = json.dumps(payload)
        super()._callDeleteApi(Api_Astral_Type.COMETH.value, json_payload)


class Soloon(AstralObject):
    def __init__(self, color="WHITE"):
        super().__init__()
        self.color = color
    
    def callPostApi(self, row, column):
        payload = {"candidateId": Constants.CANDIDATE_ID, "row": row, "column": column, "color": self.color}
        json_payload = json.dumps(payload)
        super()._callPostApi(Api_Astral_Type.SOLOON.value, json_payload)
        return
    
    def callDeleteApi(self, row, column):
        payload = {"candidateId": Constants.CANDIDATE_ID, "row": row, "column": column}
        json_payload = json.dumps(payload)
        super()._callDeleteApi(Api_Astral_Type.SOLOON.value, json_payload)
        return

class Polyanet(AstralObject):
    def __init__(self):
        super().__init__()

    def make_payload(self, row, column):
        payload = {"candidateId": Constants.CANDIDATE_ID, "row": row, "column": column}
        json_payload = json.dumps(payload)
        return json_payload
    
    def callPostApi(self, row, column):
        json_payload = self.make_payload(row, column)
        super()._callPostApi(Api_Astral_Type.POLYANET.value, json_payload)
        return
    
    def callDeleteApi(self, row, column):
        json_payload = self.make_payload(row, column)
        super()._callDeleteApi(Api_Astral_Type.POLYANET.value, json_payload)
        return





