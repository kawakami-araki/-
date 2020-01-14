import json

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
client = MongoClient()
db = client.spider


def list(requset):
    table = db.kaoshi
    manhua_list = table.find()
    print(manhua_list)
    a_list = []
    for item in manhua_list:
        a_dict = {}
        a_dict['title'] = item['title']
        a_dict['author'] = item['author']
        a_dict['content'] = item['content']
        a_list.append(a_dict)
    return JsonResponse(data={"a":a_list})