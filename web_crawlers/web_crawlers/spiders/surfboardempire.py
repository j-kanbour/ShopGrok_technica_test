import scrapy
import json

class SurfboardEmpireSpider(scrapy.Spider):
    name = 'surfboard_empire'

    start_urls = ['https://www.surfboardempire.com.au/products.json?page=1']

    def parse(self, response):
        data = json.loads(response.text)
        products = data.get('products', [])
        if products:
            for product in products:
                sku_name = product.get('title')
                product_id = product.get('id')
                brand = product.get('vendor')
                product_url = product.get('url')

                yield {
                    'Sku_name': sku_name,
                    'Product_id': product_id,
                    'Brand': brand,
                    'Product_url': product_url,
                }

            # Check if there are more pages and follow pagination
            next_page_number = int(response.url.split('=')[-1]) + 1
            next_page_url = f"https://www.surfboardempire.com.au/products.json?page={next_page_number}"
            yield scrapy.Request(url=next_page_url, callback=self.parse)