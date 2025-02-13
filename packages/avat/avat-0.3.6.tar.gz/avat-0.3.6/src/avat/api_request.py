import requests
import json

class ApiRequest:

    def __init__(self, url, header, data={}, json_flag=True):
        self.url = url
        self.header = header
        self.data = data

        self.format_data()

        if json_flag:
            self.data = json.dumps(data)
        

    def format_data(self):
        if not ("tot_eval_scores" in self.data):
            self.data["tot_eval_scores"] = {}
        if not ("aggregate_score" in self.data):
            self.data["aggregate_score"] = "0"
        if not ("eval_chat_ids" in self.data):
            self.data["eval_chat_ids"] = []

    def get(self):
        try:
            response = requests.get(self.url, headers=self.header, data="")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            return {"error ": str(e)}
    
    def post(self):
        try:
            response = requests.post(self.url, headers=self.header, data=self.data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            return {"error ": str(e)}
    