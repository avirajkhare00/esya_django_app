import requests
import json
from service1.models import NewsArticle

GET_BLOCKCHAIN_DATA = "http://104.198.180.241/query"

def get_data():

    newsArray = []

    for news in NewsArticle.objects.all():

        print news.unique_id

        params = {
            "uniqueId" : news.unique_id
        }

        r = requests.get(GET_BLOCKCHAIN_DATA, params=params)

        if r.status_code == 200:

            newsArray.append(r.text)

            print json.dumps(newsArray)

    return newsArray