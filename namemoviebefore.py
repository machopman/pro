
from pymongo import MongoClient

client = MongoClient("mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot")
db = client.moviebot

def findmovie(userid):

    cursor = db.users.find({'UserId':userid}).sort("Time")  #หาuser id
    array=[]
    for i in cursor:
        a = i
        for key, value in a.items():
            if key == 'NameMovie':
                array.append(value)


    return array[-1]
#print(findmovie('U7183997e3e85a10d8c5f1f3925825016'))

def response(question,name):

    doc = db.users.find_one({"Question":question,'NameMovie':name})
    answer=   doc['Answer']
    cate  =doc['Cate']

    return  answer ,cate

#print(response("ใครเป็นนักแสดงKanColle","KanColle"))