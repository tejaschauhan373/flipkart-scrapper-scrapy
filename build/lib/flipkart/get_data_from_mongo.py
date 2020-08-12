import pymongo
import urllib.parse
from _datetime import datetime
dt = datetime.now()
mongouri = "mongodb+srv://tejaschauhan373:" + urllib.parse.quote(
    "mongo@2020") + "@cluster0.9on8n.mongodb.net/cluster0?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongouri)

# Database name
db = client["flipkart"]

# Collection Name
col = db["mobile"]

links = []
x = col.find()
count = 1
error = 1
yesterday = []
today = []
for data in x:
    count += 1
    try:
        # print(data['ist_date_time'].date(),dt.date())
        if data['ist_date_time'].date() < dt.date():
            l = [data['model_number'], data['price'], data['display_size']]
            if l not in links:
                links.append(l)
            else:
                print(l)
        else:
            l = [data['model_number'], data['price'], data['display_size']]
            if l not in today:
                today.append(l)
            else:
                print(l)

    except:
        continue
print(len(links))
print("today", len(today))
print(count)
