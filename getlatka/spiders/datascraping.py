

import scrapy



class DatascrapingSpider(scrapy.Spider):
    name = 'datascraping'
    allowed_domains = ['www.getlatka.com']
    start_urls = ['https://getlatka.com/saas-companies?page=1']


    def parse(self, response):
        for i in response.xpath('//*[@class="data-table_table__SwBLY"]//tbody/tr'):
            # temp  =response.xpath('//*[@class="data-table_table__SwBLY"]//tbody/tr')



        # name = response.xpath("(//tr/td[2]/div/section/a)/text()").get()
            yield{
                'company_name ':  i.xpath("(td[2]/div/section/a)/text()").extract_first(),
                'revenue_name': i.xpath("(td[3]/p[1]/text())").extract()[1].strip()
            }



        # for company in response.xpath("//tr/td/section/a "):
            # name = response.xpath(".//text()").get()
            # response.css(".table.table-striped > tr:nth-child(1) > td:nth-child(2)//div[@class='cells_cell-1__9cP8o']/ul").get()

            # table = response.selector('//*[@class="data-table_table__SwBLY"]//tbody')






            # yield{
            #     "Company " :table
            #     # "Revenue" :Revenue ,
            #     # "Funding" :Funding ,
            #     # "Valuation":Valuation
            # }