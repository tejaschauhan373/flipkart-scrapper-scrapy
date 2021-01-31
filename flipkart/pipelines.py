# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import urllib.parse
from scrapy.utils.project import get_project_settings
from flipkart.settings import mongodb_srv

is_cluster_used = False
mongodb_cluster_username = None
mongodb_cluster_password = None
mongodb_cluster_url = None

if "cluster" in mongodb_srv:
    mongodb_cluster_username = mongodb_srv.split("mongodb+srv://")[-1].split(":")[0]
    mongodb_cluster_password = mongodb_srv.split("mongodb+srv://")[-1].split(":")[-1].split('@')[0]
    mongodb_cluster_url = mongodb_srv.split("mongodb+srv://")[-1].split(":")[-1].split('@')[-1]
    is_cluster_used = True

mongouri = mongodb_srv

if is_cluster_used:
    mongouri = f"mongodb+srv://{mongodb_cluster_username}:" + urllib.parse.quote(
        f"{mongodb_cluster_password}") + f"@{mongodb_cluster_url}"


class FlipkartPipeline:
    def process_item(self, item, spider):
        return item


settings = get_project_settings()

print("mongodb_srv", mongodb_srv)

class MongoDBPipeline(object):

    def __init__(self):
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
