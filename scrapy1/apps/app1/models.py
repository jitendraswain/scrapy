from locale import currency
from django.db import models
from pytz import country_names


# Create your models here.

class Covid(models.Model):
    country_name = models.CharField(max_length=100,null=True,blank=True)
    total_cases = models.CharField(max_length=100,null=True,blank=True)
    total_deaths = models.CharField(max_length=100,null=True,blank=True)
    recovered = models.CharField(max_length=100,null=True,blank=True) 
    new_cases = models.CharField(max_length=100,null=True,blank=True)

class Currency(models.Model):
    country_name = models.CharField(max_length=56,null=True,blank=True)
    currency = models.CharField(max_length=56,null=True,blank=True)

class History(models.Model):
    currency = models.ForeignKey('currency',null=True,blank=True,on_delete=models.CASCADE)
    covid = models.ForeignKey('covid',null=True,blank=True,on_delete=models.CASCADE)