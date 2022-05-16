from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import subprocess
from apps.app1.serializers import SocialRegistrationSerializer
# Create your views here.
import requests
class ScrapeCoronaViewset(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        data = subprocess.call('/var/www/html/project/scrapy1/spyder.sh',shell=True)
        return Response({'data':data})

class ScrapeCurrencyViewset(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        data = subprocess.call('/var/www/html/project/scrapy1/spyder2.sh',shell=True)

        return Response({'data':data})

class ScrapeCurrencyCodeViewset(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        
        try:
            data=requests.post(url='https://www.html-code-generator.com/js/ajax/json/country/all.json')
            json_data = data.json()
            print(json_data)
            list_dict=[]
            for obj in json_data:
                # print(obj.get('name'))
                dict_data ={}
                dict_data['name']=obj.get('name')
                list_dict.append(dict_data)
            print(list_dict)
            return Response({'data':'ok'})
        except Exception as e:
            raise e