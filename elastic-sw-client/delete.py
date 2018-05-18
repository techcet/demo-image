from elasticsearch import Elasticsearch
import os

NAMESPACE = "NAMESPACE" in os.environ

es = Elasticsearch(['elasticsearch.{}.svc.cluster.local:9200'.format(os.environ['NAMESPACE'])])

print("Deleting Book 1")
res = es.delete(index="sidious", doc_type="tome", id=1)

print("Deleting Book 2")
res = es.delete(index="sidious", doc_type="tome", id=2)
