from django.shortcuts import render
import requests
import os
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from decouple import config
from django.http import HttpResponse
# Create your views here.

access_key = config("ACCESS_TOKEN")
@api_view(('GET',))
def getAccessScopes(request):
    print(config)
    url = "https://python-test-shop.myshopify.com/admin/oauth/access_scopes.json"
    payload = {
                
            }
    print(access_key)
    headers = {
        "X-Shopify-Access-Token":access_key,
        "content-type": "application/json"
        }
    print(headers)
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print(" Status Success")
    elif r.status_code == 401:
        print(" Invalid or Unauthrized Access Key")
    elif r.status_code == 403:
        print("You dont have permission to access this data")
    # print("read_inventory" in r.json()['access_scopes'][0].values())
    # print(r.json()['access_scopes'])
    # for each in r.json()['access_scopes']:
    #     if "read_inventory" in each.values():
    #         print('--------------------')
    return HttpResponse('Hello! ' * times)


@api_view(["GET"])
def getAllProducts(request):
    url = "https://python-test-shop.myshopify.com/admin/api/2022-04/products.json"
    headers = {
        "X-Shopify-Access-Token":access_key,
        "content-type": "application/json"
        }
    print(headers)
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        with open('new_file.json', 'w') as f:
            json.dump(r.json(), f, indent=2)
            print("New json file is created from data.json file")
        print(" Status Success")
    elif r.status_code == 401:
        print(" Invalid or Unauthrized Access Key")
    elif r.status_code == 403:
        print("You dont have permission to access this data")
    
    return HttpResponse('Hello! ')