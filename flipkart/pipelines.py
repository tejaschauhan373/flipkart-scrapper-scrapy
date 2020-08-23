# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import urllib.parse
from scrapy.utils.project import get_project_settings


class FlipkartPipeline:
    def process_item(self, item, spider):
        return item

settings = get_project_settings()

class MongoDBPipeline(object):

    def __init__(self):
        mongouri = "mongodb+srv://tejaschauhan373:" + urllib.parse.quote(
            "mongo@2020") + "@cluster0.9on8n.mongodb.net/cluster0?retryWrites=true&w=majority"
        connection = pymongo.MongoClient(mongouri)
        try:
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODB_COLLECTION']]
        except:
            db = connection['flipkart']
            self.collection = db['mobile']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item