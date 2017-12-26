from scrapy import Spider, Request


class TestDev(Spider):
    name = "quotes"

    def start_requests(self):
        urls = ['https://whatismyipaddress.com/']
        for url in urls:
            request = Request(url=url, callback=self.parse)
            request.meta["proxy"] = "http://165.227.186.129:80"
            yield request

    def parse(self, response):
        ip = response.xpath("//div[@id='main_content']/div[@id='section_left']/div[2]/a//text()").extract_first()
        print("Your ip {}".format(ip))
        return
