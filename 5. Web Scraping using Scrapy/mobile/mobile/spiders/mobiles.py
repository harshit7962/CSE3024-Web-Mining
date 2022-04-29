import scrapy
import urllib


class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    allowed_domains = ['www.amazon.in/s?k=mobile']
    start_urls = ['http://www.amazon.in/s?k=mobile/']

    def parse(self, response):
        i=0
        image = response.css(".s-image-fixed-height .s-image::attr(src)")[i].extract()
        discount = response.css(".a-letter-space+ span::text")[i].extract()
        name = response.css(".a-color-base.a-text-normal::text")[i].extract()
        price = response.css(".a-price-while::text")[i].extract()
        
        print("Name: ", name)
        print("Price: ", price)
        print("Discount: ", discount)
        print("Image URL: ", image)
        f = open('img.jpg', 'wb')
        f.write(urllib.request.urlopen(image).read())
