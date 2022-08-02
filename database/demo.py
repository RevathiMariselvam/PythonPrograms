import pymongo
con=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=con["StudentDatabase"]
mycol=mydb["Student personal details"]
data={"_id":2001,"name":"revathi","age":20,"dept":"cse"}
data1={"_id":2003,"name":"ayathri","age":30,"dept":"IT"}
mycol.insert_one(data1)
print("data inserted")