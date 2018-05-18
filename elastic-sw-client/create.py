from elasticsearch import Elasticsearch
import os

NAMESPACE = "NAMESPACE" in os.environ

es = Elasticsearch(['elasticsearch.{}.svc.cluster.local:9200'.format(os.environ['NAMESPACE'])])

book1 = { 'author': 'sidious', 'title': 'Convert Jedi to Dark Side: 101' }
book2 = { 'author': 'sidious', 'title': 'Welcome to the Dark Side' }

print("Creating/Updating Books")
res = es.index(index="sidious", doc_type="tome", id=1, body=book1)
print(res['result'], ": ", res)

res = es.index(index="sidious", doc_type="tome", id=2, body=book2)
print(res['result'], ": ", res)
