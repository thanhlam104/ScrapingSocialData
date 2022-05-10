import scrapy
from scrapy import Request

class RgSpider(scrapy.Spider):
    name = 'RG'
    allowed_domains = ['https://www.researchgate.net/']
    url = 'https://www.researchgate.net/institution/Hanoi-University-of-Science-and-Technology/members'
    
    def start_requests(self):
        for i in range (27):
            yield Request(self.url+f'/{i+1}', callback=self.parse_list)
    
    def parse_list(self, response):
        profile_links = response.css('.nova-legacy-e-text--size-l a::attr(href)').getall()
        for link in profile_links:
            yield Request('https://www.researchgate.net/'+link, callback=self.parse_profile)
    
    def parse_profile(self, response):
        print('S.O.S')
        name = response.css('div.nova-legacy-e-text--size-xxl').get()
        yield {
            'name': name
        }