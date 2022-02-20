import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Everybody:arsenalB2@cluster0.wijun.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["Content"]
mycol = mydb["Import"]

# mydict = [
#     {
#         'name': 'Ugwudike Favour',
#         'age': 21,
#         'height': '180 cm',
#         'weight': '62 kg'
#     },
#     {
#         'name': 'Ugwudike Gift',
#         'age': 20,
#         'weight': '58 kg'
#     },
#     {
#         'name': 'Ugwudike Honour',
#         'age': '18',
#         'height': '159 cm'
#     }
# ]

# mycol1 = mycol.insert_many(mydict)

# print(mycol1.inserted_ids)
#print(mycol1.inserted_id)

# for x in mycol.find({}, {'_id': 0, 'name': 1, 'height': 1, 'age': 1, 'weight': 1}):
#     print(x)

# myquery = {'age': {'$gt': 18}}

# for x in mycol.find(myquery).sort('age', -1):
#     print(x)

# myquery = {'name': 'Ugwudike Honour'}
# updatequery = {'$set': {'age': 18}}

# mycol.find_one_and_update(myquery, updatequery)

for x in mycol.find({}, {'_id': 0}).sort('age', -1):
    print(x)