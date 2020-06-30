from elasticsearch import Elasticsearch, helpers
import json
from io import StringIO

# ES IP주소와 포트(9200)로 연결한다.
es = Elasticsearch("localhost:9200")
es.info()

# index 생성(존재시 pass)
def make_index(es, index_name, mapping):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    print(es.indices.create(index=index_name, body=mapping))

def insertData():
    es = Elasticsearch('localhost:9200')
    index="seoul-metro-logs-2019"
    with open('./index-settings-mappings.json', 'r') as f:
        mapping = json.load(f)
    
    make_index(es, index, mapping)

    with open('/home/ec2-user/elastic-demos/seoul-metro-logs/data/seoul-metro-2019.logs', 'r') as logfile:
        for line in logfile:
            line = StringIO(line)
            doc = json.load(line)
            es.index(index="seoul-metro-logs-2019", doc_type="_doc", body=doc)
            #document = json.load(logfile)
    
    # for doc in document:
    #     es.index(index="seoul-metro-logs-2019", doc_type="_doc", body=doc)

    # for _, i in enumerate(document):
    #     doc = {"@timestamp":i["@timestamp"],
    #     "code":i["code"],
    #     "line_num":i["line_num"],
    #     "line_num_en":i["line_num_en"],
    #     "station":{"name":i["name"],"kr":i["kr"],
    #         "en":i["en"],"chc":i["chc"],
    #         "ch":i["ch"],"jp":i["jp"]},
    #     "location":{"lat":i["lat"],"lon":i["lon"]},
    #     "people":{"in":i["in"],"out":i["out"],"total":i["total"]}}
    #     es.index(index="seoul-metro-logs-2019", doc_type="_doc", body=doc)
   

insertData()