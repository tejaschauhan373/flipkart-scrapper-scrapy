import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["flipkart"]

# Collection Name
col = db["mobile"]

links=[]
x = col.find()
count=1
for data in x:
    if data['url'] in links:
        print(data['url'])
    else:
        links.append(data['url'])
print(len(links))
