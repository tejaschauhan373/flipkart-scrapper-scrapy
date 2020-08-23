import pymongo
import urllib.parse
from datetime import datetime

current_date = datetime(2020, 8, 23)  # (yy,mm,dd)

mongouri = "mongodb+srv://AkshatMehta:" + urllib.parse.quote(
    "AkshatMehtaProjectOne") + "@cluster0.9on8n.mongodb.net/cluster0?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongouri)

# Database name
db = client["flipkart"]

# Collection Name
col = db["mobile"]

before_current_date=datetime(2020, 8,22)
after_current_date=datetime(2020, 8,24)
x = col.find({"ist_date_time":{"$gt": before_current_date, "$lt":after_current_date}})
count = 0
for data in x:
    if data['ist_date_time'].date() == current_date.date():
        count += 1
print(f"Total items inserted on {current_date} is {count}")
