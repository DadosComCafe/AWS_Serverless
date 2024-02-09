from pymongo import MongoClient
user = "dadoscomcafedev"
password = "androide93"
myclient = MongoClient(f"mongodb+srv://{user}:{password}@dadoscomcafe.3vicyiz.mongodb.net/")

mydb = myclient["youtubecomments"]
mycol = mydb["videos_to_analyse"]
x = mycol.find_one({"analyzed": False})
print(x)