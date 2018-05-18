from elasticsearch import Elasticsearch
import os

NAMESPACE = "NAMESPACE" in os.environ

es = Elasticsearch(['elasticsearch.{}.svc.cluster.local:9200'.format(os.environ['NAMESPACE'])])

book1 = { 'author': 'sidious', 'title': 'Convert Jedi to Dark Side: 101' }
book2 = { 'author': 'sidious', 'title': 'Welcome to the Dark Side' }

print("Searching for Books by Darth Sidious")
res = es.search(index="sidious", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit)

print("Get Book 1 by Darth Sidious")
res = es.get(index="sidious", doc_type="tome", id=1)
print(res['_source'])
