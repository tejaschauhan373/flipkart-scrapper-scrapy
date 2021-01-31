# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    price = Field()
    color = Field()
    model_name = Field()
    model_number = Field()
    secondary_camera = Field()
    primary_camera = Field()
    battery_size = Field()
    height = Field()
    weight = Field()
    depth = Field()
    width = Field()
    resolution_type = Field()
    display_size = Field()
    storage = Field()
    ram = Field()
    operating_system = Field()
    processor = Field()
    ist_date_time = Field()
    utc_time_stamp = Field()
    feature_rating = Field()
    rating = Field()
    other = Field()
    company = Field()
