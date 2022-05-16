# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from apps.app1.models import Covid

class Worldometer2(scrapy.Item):
    pass


class CovidItem(DjangoItem):
        django_model = Covid