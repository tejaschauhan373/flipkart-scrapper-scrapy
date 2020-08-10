from flipkart.items import *
import traceback
import re
import scrapy
from datetime import timezone
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ScrapeflipkartSpider(scrapy.Spider):
    name = 'scrapeflipkart'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi',
                  "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme",
                  "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1",
                  # "https://www.flipkart.com/oppo-mobile-phones-store?otracker=nmenu_sub_Electronics_0_OPPO",
                  "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&wid=1.productCard.PMU_V2_1",
                  "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3D15000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&wid=2.productCard.PMU_V2_2",
                  "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&sid=tyy%2F4io&wid=4.productCard.PMU_V2_4",
                  "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D15000&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&wid=3.productCard.PMU_V2_3",
                  "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo"]

    rules = (Rule(LinkExtractor(restrict_xpaths=['//a[contains(text(),"Previous")]']), follow=True),)
    def parse(self, response):
        mobile_links = response.xpath('//*[@class="_31qSD5"]/@href').extract()
        # print(mobile_links)
        mobile_links = [response.urljoin(i) for i in mobile_links]

        # print(mobile_links)
        next_page_text = response.xpath('//a[@class="_3fVaIS"]/span/text()').extract()
        next_page_url=response.xpath('//a[@class="_3fVaIS"]/@href').extract()
        print(next_page_url, next_page_text)
        for i in mobile_links:
            yield scrapy.Request(i, callback=self.scrape_mobile_page)
        if len(next_page_text)>0 and next_page_text[-1].strip()=="Next":
            next_page_url = response.urljoin(next_page_url[-1])
            if next_page_url[-1] != response.request.url:
                yield scrapy.Request(next_page_url, callback=self.parse)
        # else:
        # yield scrapy.Request(self.all_mobile_links[0],callback=self.parse_main_page)


    def scrape_mobile_page(self, response):
        item = FlipkartItem()
        if re.match(r'Mi', response.xpath('//title/text()').extract_first()):
            item['company'] = "Mi"
        elif re.match(r'Realme', response.xpath('//title/text()').extract_first()):
            item['company'] = "Realme"
        elif re.match(r'Vivo', response.xpath('//title/text()').extract_first()):
            item['company'] = "Vivo"
        elif re.match(r'OPPO', response.xpath('//title/text()').extract_first()):
            item['company'] = "OPPO"
        elif re.match(r'Samsung', response.xpath('//title/text()').extract_first()):
            item['company'] = "Samsung"
        other = {}
        item['url'] = response.request.url

        for i in response.xpath('//tr[@class="_3_6Uyw row"]'):
            data = i.xpath('.//text()').extract()
            if data[0] == "RAM":
                try:
                    item['ram'] = int(data[-1].split()[0])
                except ValueError:
                    item['ram'] = data[-1].split()
            elif data[0] == "Battery Capacity":
                item['battery_size'] = int(data[-1].split()[0])
            elif data[0] == "Color":
                item['color'] = data[-1]
            elif data[0] == "Model Number":
                item['model_number'] = data[-1].split('/')
            elif data[0] == "Model Name":
                item['model_name'] = data[-1]
            elif data[0] == "Height":
                try:
                    item['height'] = float(data[-1].split()[0])
                except ValueError:
                    traceback.print_exc()
                    item['height'] = data[-1]
            elif data[0]=="Width":
                try:
                    item['width']=float(data[-1].split()[0])
                except ValueError:
                    traceback.print_exc()
                    item['width']=data[-1]
            elif data[0] == "Weight":
                try:
                    item['weight'] = float(data[-1].split()[0])
                except ValueError:
                    traceback.print_exc()
                    item['height'] = data[-1]
            elif data[0] == "Depth":
                try:
                    item['depth'] = float(data[-1].split()[0])
                except ValueError:
                    traceback.print_exc()
                    item['depth'] = data[-1]
            elif data[0] == "Internal Storage":
                try:
                    item['storage'] = int(data[-1].split()[0])
                except ValueError:
                    traceback.print_exc()
                    item['storage'] = data[-1]
            elif data[0] == "Processor Type":
                item['processor'] = data[-1]
            elif data[0] == "Operating System":
                item['operating_system'] = data[-1]
            elif data[0] == "Secondary Camera":
                item['secondary_camera'] = [int(re.findall(r'\d+', i)[0]) for i in re.findall(r'\d+MP', data[-1])]
            elif data[0] == "Primary Camera":
                item['primary_camera'] = [int(re.findall(r'\d+', i)[0]) for i in re.findall(r'\d+MP', data[-1])]
            elif data[0] == "Display Size":
                size = {}
                if re.findall('\d+[.]*\d* cm', data[-1]):
                    cm = re.findall('\d+[.]*\d* cm', data[-1])
                    cm = cm[0].split()
                    size[cm[-1]] = float(cm[0])
                if re.findall('\d+[.]*\d* inch', data[-1]):
                    inch = re.findall('\d+[.]*\d* inch', data[-1])
                    inch = inch[0].split()
                    size[inch[-1]] = float(inch[0])
                item['display_size'] = size
            elif data[0] == "Resolution Type":
                item['resolution_type'] = data[-1]
            else:
                if not len(data[0]) > 50:
                    if data[-1].strip() == "Yes":
                        other[data[0]] = True
                    elif data[-1].strip() == "No":
                        other[data[0]] = False
                    else:
                        other[data[0]] = data[-1]
        ist_dt = datetime.datetime.now()
        utc_time = ist_dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        item['ist_date_time'] = ist_dt
        item['utc_time_stamp'] = utc_timestamp
        item['other'] = other
        feature_tags = response.xpath('//div[@class="_1nl9s1"]')
        feature_rating = {}
        for i in feature_tags:
            try:
                feature_rating[i.xpath('.//div[@class="_3wUVEm"]/text()').extract_first()] = float(
                    i.xpath('.//text[@class="PRNS4f"]/text()').extract_first())
            except ValueError:
                feature_rating[i.xpath('.//div[@class="_3wUVEm"]/text()').extract_first()] = i.xpath(
                    './/text[@class="PRNS4f"]/text()').extract_first()
            item['feature_rating'] = feature_rating
        item['rating'] = float(response.xpath('//div/div[@class="_1i0wk8"]/text()').extract_first())
        item['price'] = int(
            "".join(response.xpath('//div[@class="_1vC4OE _3qQ9m1"]/text()').extract_first()[1:].split(',')))
        yield item
