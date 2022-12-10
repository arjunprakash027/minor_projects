from pymongo import MongoClient
from urllib.parse import quote
from bson.objectid import ObjectId

cluster = "mongodb://localhost/"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.test_db

print(db.list_collection_names())

example = {
    "name":"Arjun",
    "age":"20",
    "intrests":["programming","gamming","watching movies"]
}

#insert = db.insert

#result = insert.insert_one(example)

example2 = [
{
    "name":"sushmeetha",
    "age":"19",
    "intrests":["series","gaming","novels"]
},
{
    "name":"Naveen",
    "age":"20",
    "intrests":["anime","programming","UV"]
}]

datails = db.datails
result = datails.insert_many(example2)

'''
result = insert.find({"intrests":"programming"})
print(result)

result2 = insert.find_one({"_id":ObjectId('62e234e16af7d260beb05e14')})
print(result2)

for i in result:
    print(i)

print(insert.count_documents({})) #to print all put curly braces

print(insert.count_documents({"intrests":"programming"})) #to print some put curly braces


#result3 = insert.delete_one({"name":"Naveen"})

#result4 = insert.delete_many({}) #delete all

result5 = insert.update_one({"name":"Arjun"},{"$set":{"name":"Arjun rao"}})
'''