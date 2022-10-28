#Spider code
import scrapy

class melata(scrapy.Spider):
    name = 'melatakuys' #nama spider
    start_urls = ["https://store.playstation.com/en-id/search/tekken/"] #url awal
    

    def parse(self, response):
        url = response.url
        
        for i in range(1,3): #iterasi sampe page ke-46
            yield scrapy.Request(url=url+str(i), callback=self.parse_details) #url awal ditambah page ke-sekian
            
    def parse_details(self, response):
        for text in response.css(".psw-product-tile"): 
            yield{
                "title":text.css(".psw-t-body::text").get(), #filter yang memiliki class .psw-t-body
                "price":text.css(".psw-m-r-3::text").get()}  #filter yang memiliki class .psw-m-r-3
        pass

