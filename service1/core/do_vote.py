import requests
import json

CHAINCODE_URL = "http://104.198.180.241/transactions/"
GET_BLOCKCHAIN_DATA = "http://104.198.180.241/query"

class DoVote:

    def __init__(self, request, unique_id, status):

        params = {
            "uniqueId": unique_id
        }

        r = requests.get(GET_BLOCKCHAIN_DATA, params=params)

        if r.status_code == 200:

            data = json.loads(r.text)

            data_value = json.loads(data['value'])
            post_data = {
                "key": data_value['key_reference'],
                "jsonString": {
                    "key_reference": data_value['key_reference'],
                    "news_title": data_value['news_title'],
                    "news_url": data_value['news_url'],
                    "news_category": data_value['news_category'],
                }
            }

            if status == "upvote":

                post_data['jsonString']['upvotes'] = str(int(data_value['upvotes']) + 1)
                post_data['jsonString']['downvotes'] = data_value['downvotes']


            if status == "downvote":


                post_data['jsonString']['upvotes'] = data_value['upvotes']
                post_data['jsonString']['downvotes'] = str(int(data_value['downvotes']) - 1)

            post_data['jsonString'] = json.dumps(post_data['jsonString'])


            s = requests.post(CHAINCODE_URL, headers = {"Content-Type": "application/json"}, data=json.dumps(post_data))

            if s.status_code == 200:

                print "transaction is successful"
                print s.text