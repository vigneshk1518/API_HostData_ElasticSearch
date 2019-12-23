from django.conf import settings
from elasticsearch import Elasticsearch
import requests, json
from random import randint
import time, schedule

# from hostdata.models import Host_Data
# ES_INDEX = settings.ES_INDEX
BASE_URL = "http://10.11.100.46:9200/"
ENDPOINT = "hostindex/"

es = Elasticsearch(hosts="http://10.11.100.46/", retry_on_timeout=True)

class HostDocument():
    # class Meta:
    #     model = Host_Data  # The model associated with this DocType

    def esdata_scheduler():
        print("I'm in Scheduler function...")

        # Scheduler for es_data_post( function to push data every 60 seconds
        schedule.every(1).minutes.do(esdata_post)

        # Scheduler for es_data_get( function to push data every 1 hour
        schedule.every(2).hour.do(esdata_get)

    def esdata_post(self):
        BASE_URL = "http://10.11.100.46:9200/"
        ENDPOINT = "hostindex/"
        headers = {'content-type': 'application/json'}
        #To generate values randomly
        for i in range(5):
            host_data = {
                    "hcpu_clk": randint(50000,70000),
                    "hmem_ram": randint(20000,30000)
                         }

            print("The Data Pushed to Elastic Search :", host_data)

            # API to push host parameters to Elastic Search :", host_data)
            resp = requests.post(BASE_URL + ENDPOINT + 'doc', data=json.dumps(host_data))
            print(resp.url)
            print(resp.text)
            print(resp.status_code)


    ## API to get the parameters from Elastic Search

    def esdata_get(uri, hcpu_clk):
        query = json.dumps({
        "query": {
            "match": {
                "content": hcpu_clk
                    }
                }
                        })
        uri = "http://10.11.100.46:9200/hostindex/_search"
        response = requests.get(uri)
        result_data = json.loads(response.text)
        print("The Data Extracted from Elastic Search is :", result_data)
        return result_data


obj = HostDocument()

# obj.esdata_scheduler()
obj.esdata_post()
obj.esdata_get(None)
