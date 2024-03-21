import scrapy

class AldiSpider(scrapy.Spider):
    name = 'aldi'
    start_urls = ['https://www.aldi.com.au/']

    def parse(self, response):
        groceries = response.xpath("//li[@class='main-nav--item ym-clearfix product-range is-closed is-first-level']")
        
        for sub_category in groceries.xpath("./div[2]/ul/li/div[1]/a[1]/@href"):
            yield response.follow(sub_category, self.parse_item)

    def parse_item(self, response): 
        for product_tile in response.xpath('//div[@class="tx-aldi-products"]/div/a'):
            Product_title = product_tile.xpath('.//div[@class="box--description--header"]/text()').get().strip()
            Product_image = product_tile.xpath('.//img/@src').get()
            Packagesize = product_tile.xpath('.//span[@class="box--amount"]/text()').get()
            Price = product_tile.xpath('.//span[@class="box--value"]/text()').get()
            Price_decimal = product_tile.xpath('.//span[@class="box--decimal"]/text()').get()
            Price_per_unit = product_tile.xpath('.//span[@class="box--baseprice"]/text()').get()
            
            # Concatenate Price and Price_decimal to get the complete price
            Price = Price + (Price_decimal if Price_decimal else '')
            
            yield {
                'Product_title': Product_title,
                'Product_image': Product_image,
                'Packagesize': Packagesize,
                'Price': Price,
                'Price_per_unit': Price_per_unit,
            }
