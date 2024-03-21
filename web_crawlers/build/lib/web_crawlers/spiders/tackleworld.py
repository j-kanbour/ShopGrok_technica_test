import scrapy
import re

class tackleWrldSpider(scrapy.Spider):
    name = 'tackleWorld'

    start_urls = ['https://tackleworldadelaide.com.au/']

    def parse(self, response):

        #search through all sub cateories
        for menu in response.xpath("//a[@class='navPage-subMenu-action navPages-action has-subMenu']/@href"):

            yield response.follow(menu, self.parse_item)
        
    def parse_item(self, response): 

        for product_tile in response.xpath('//li[@class="product"]'):

            sku_name = product_tile.xpath('.//h4/a/text()').get().strip()
            image_url = product_tile.xpath('.//img/@src').get()

            price_now = product_tile.xpath('.//span[@class="price"]/text()').get().strip()
            price_was = product_tile.xpath('.//span[@class="price price--rrp"]/text()').get()
            product_url = product_tile.xpath('.//h4/a/@href').get()
            
            price_now_value = re.search(r'\d+\.\d+', price_now).group() if price_now else None
            price_was_value = re.search(r'\d+\.\d+', price_was).group() if price_was else None

            yield {
                'Sku_name': sku_name,
                'Image_url': image_url,
                'Price_now': price_now_value,
                'Price_was': price_was_value,
                'Product_url': product_url,
            }
