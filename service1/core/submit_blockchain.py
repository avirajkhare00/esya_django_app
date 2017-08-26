import requests
import json

CHAINCODE_URL = "http://104.198.180.241/transactions/"

class SubmitBlockchain:

    def __init__(self, request, unique_id):

        post_data = {
            "key" : unique_id,
            "jsonString" : json.dumps({
                "key_reference" : unique_id,
                "news_title" : request['newsTitle'],
                "news_url" : request['newsUrl'],
                "news_category" : request['newsCategory'],
                "upvotes" : "0",
                "downvotes" : "0"
            })
        }

        r = requests.post(CHAINCODE_URL, headers = {"Content-Type": "application/json"}, data=json.dumps(post_data))

        if r.status_code == 200:

            print "transaction is successful"

            print r.text

        else:

            print "something went wrong nodejs client!"
