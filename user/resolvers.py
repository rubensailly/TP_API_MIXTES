import json

def get_users(_, info):
    with open('{}/data/users.json'.format("."), "r") as jsf:
        users = json.load(jsf)["users"]
        return users

def get_userid(_, info, _id):
    with open('{}/data/users.json'.format("."), "r") as jsf:
        users = json.load(jsf)["users"]
        for user in users:
            if str(user["id"]) == str(_id):
                return user