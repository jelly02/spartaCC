from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

# CREATE
# db.users.insert_one({'name':'Jane','age':23})
# db.users.insert_one({'name':'James','age':40})
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})

# READ
all_users = list(db.users.find({})), # 해당 db 정보 전체 가져오기, {'_id':False} = id는 가져오지 않음
#print(all_users) #{'_id': ObjectId('5f1bf3f354d25a1b498983e0'), 'name': 'Jane', 'age': 23}

# all_user의 전체가져오기
for user in all_users:
    print(user)


# 한 사람만 가져오기
#person =db.users.find_one({'name':'James'})
#print(person)

# UPDATE
#db.users.update_one({'name':'James'},{'$set':{'age':41}})
#james = db.users.find_one({'name':'James'})
#print(james)

# DELETE
#db.users.delete_one({'name' : 'James'})
#person = db.users.find_one({'name' : 'James'}) #잘 삭제 됐는지 확인
#print(james)