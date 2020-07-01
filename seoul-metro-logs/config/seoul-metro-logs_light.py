from elasticsearch6 import Elasticsearch, helpers
import json
import pprint
from io import StringIO

# ES IP주소와 포트(9200)로 연결한다.
es = Elasticsearch("localhost:9200")

def insertData():
    index="seoul-metro-logs-2019"

    with open('/home/ec2-user/nclab/elastic-demos/seoul-metro-logs/data/seoul-metro-2019.logs', 'r') as logfile:
        for line in logfile:
            line = StringIO(line)
            doc = json.load(line)
            es.index(index="seoul-metro-logs-2019", doc_type="_doc", body=doc)

insertData()