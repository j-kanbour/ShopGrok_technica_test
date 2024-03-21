import scrapy
import google.cloud

class tackleWorldSpider(scrapy.Spider):
    name = 'tackleWorld'

    start_urls = ['https://tackleworldadelaide.com.au/']

    def parse(self, response):

        #traverse all sub categories
        for menu in response.xpath("//a[@class='navPage-subMenu-action navPages-action has-subMenu']/@href"):

            try:
                yield response.follow(menu, self.parse_item)
            except:
                continue
        
    def parse_item(self, response): 

        for product_tile in response.xpath('//li[@class="product"]'):

            sku_name = product_tile.xpath('.//h4/a/text()').get().strip()
            image_url = product_tile.xpath('.//img/@src').get()
            price_now = product_tile.xpath('.//span[@class="price"]/text()').get().strip()
            price_was = product_tile.xpath('.//span[@class="price price--rrp"]/text()').get()
            product_url = product_tile.xpath('.//h4/a/@href').get()
            
            yield {
                'Sku_name': sku_name,
                'Image_url': image_url,
                'Price_now': price_now,
                'Price_was': price_was,
                'Product_url': product_url,
            }
