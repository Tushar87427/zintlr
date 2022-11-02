import scrapy
class DatascrapingSpider(scrapy.Spider):
    name = 'datascraping'
    allowed_domains = ['www.getlatka.com']
    start_urls = ['https://getlatka.com/saas-companies?page=%d' % j for j in range(1,1310)]


    def parse(self, response):
        for i in response.xpath('//*[@class="data-table_table__SwBLY"]//tbody/tr'):



            yield{
                'company_name ':  i.xpath("(td[2]/div/section/a)/text()").extract_first() if  i.xpath("(td[2]/div/section/a)/text()").extract_first() else  " ",
                'revenue': i.xpath("(td[3]/p[1]/text())").extract()[1].strip() if i.xpath("(td[3]/p[1]/text())").extract()[1].strip() else " ",
                'funding': i.xpath("(td[4]/p[1]/text())").extract()[1].strip() if i.xpath("(td[4]/p[1]/text())").extract()  else "" ,
                'Valuation': i.xpath("(td[5]/p[1]/text())").extract()[1].strip() if i.xpath("(td[5]/p[1]/text())").extract() else " ",
                'funder': i.xpath("(td[7]/div/a/text())").extract_first() if i.xpath("(td[7]/div/a/text())").extract_first() else " ",
                "Team Size" : i.xpath("(td[8]/p[1]/text())").extract()[1].strip() if i.xpath("(td[8]/p[1]/text())").extract()[1].strip() else " "
            }







