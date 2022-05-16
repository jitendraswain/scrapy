from itertools import count
from os import stat_result
from wsgiref import headers
from pytz import country_names
import scrapy
from apps.app1.models import Covid,Currency

data_list = []

class CoranavirusSpider(scrapy.Spider):
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    name = 'coranavirus'
    allowed_domains = ['www.worldometers.info']
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    name = 'coranavirus'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus']
    # def parse(self, response):
        
    #     for country in response.xpath("(//table[@id='main_table_countries_today']/tbody)[1]//tr"):
    #         name = country.xpath(".//td/a[@class='mt_a']/text()").get()
    #         url_link = country.xpath(".//td/a[@class='mt_a']/@href").get()
    #         if name is None:
    #             name = country.xpath(".//td/span/text()").get()
    #         url_link = response.urljoin(url_link)
        
    #         if name:
    #             name = country.xpath(".//td/a[@class='mt_a']/text()").get()
    #             new_cases = country.xpath(".//td[4]/text()").get()
    #             total_recovered = country.xpath(".//td[7]/text()").get()
    #             if total_recovered is None:
    #                 total_recovered = country.xpath(".//td[7]/span/text()").get()

    #             yield restart_urls = ['https://www.worldometers.info/coronavirus']
    def parse(self, response):
        
        for country in response.xpath("(//table[@id='main_table_countries_today']/tbody)[1]//tr"):
            name = country.xpath(".//td/a[@class='mt_a']/text()").get()
            url_link = country.xpath(".//td/a[@class='mt_a']/@href").get()
            if name is None:
                name = country.xpath(".//td/span/text()").get()
            url_link = response.urljoin(url_link)
        
            if name:
                name = country.xpath(".//td/a[@class='mt_a']/text()").get()
                new_cases = country.xpath(".//td[4]/text()").get()
                total_recovered = country.xpath(".//td[7]/text()").get()
                if total_recovered is None:
                    total_recovered = country.xpath(".//td[7]/span/text()").get()
                yield response.follow(url=url_link,callback=self.page2parser,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'},meta={'country_name':name,'new_cases':new_cases})


    def page2parser(self, response):
        country_name = response.request.meta["country_name"]
        new_cases = response.request.meta["new_cases"]
        total_cases = response.xpath("(//div[@class='maincounter-number'])[1]/span/text()").get()
        deaths = response.xpath("(//div[@class='maincounter-number'])[2]/span/text()").get()
        recovered = response.xpath("(//div[@class='maincounter-number'])[3]/span/text()").get()
        model_obj,obj = Covid.objects.get_or_create(
            country_name = country_name,
            )
        model_obj.total_cases= total_cases,
        model_obj.total_deaths = deaths,
        model_obj.recovered = recovered,
        model_obj.new_cases= new_cases
        model_obj.save()
        # print(model_obj)
        # yield{
        #     'country_name':country_name,
        #     'total_cases':total_cases,
        #     'total_deaths':deaths,
        #     'recovered':recovered,
        #     'new_cases':new_cases
        #     }

class CurrenciesSpider(CoranavirusSpider):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    name = 'currencies'
    allowed_domains = ['www.countries-ofthe-world.com']
    start_urls = ['https://www.countries-ofthe-world.com/world-currencies.html']
    data_list = []
    def parse(self,response):
    
        for currency in response.xpath("//div[@id='mainwrap']/div[@id='contentarea']/div[@id='centercolumn']/div[@id='content']/div[@class='container']/table//tr"):
            # data={}
            country_names = currency.xpath(".//td[1]/text()").get()
            currency = currency.xpath(".//td[3]/text()").get()
            # data['country_names']=country_names
            # data['currency']=currency
            Currency.objects.get_or_create(
                country_name = country_names,
                currency = currency)
            # data_list.append(data)
        # print(data_list)
        # output = [{k: v for k, v in var.items() if v is not None} for var in data_list]
        # for x,y in enumerate (output):
            # print(x,y)
            # print(y,len(y))
            # if len(y) == 0 :for x,y in enumerate (output):
        #     # print(x,y)
        #     # print(y,len(y))
        #     if len(y) == 0 :
                # del output[x]
            # if len(y) == 1 :
                # del output[x]
        # output2 = [{k: v for k, v in var.items() if v is not None} for var in output]
        # del output[0]
        # print(output)   