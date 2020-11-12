import requests
from common.cfg import *


class Login(object):
    def __init__(self):
        pass
    def login(self,username,psw):
        url = HOST + "/api/v1/user/login"
        body = {
              "password": MNFInfo[1],
              "username": MNFInfo[0]
            }
        res = requests.post(url,json=body)
        dict = res.json()['data']
        return dict
if __name__ == '__main__':
    l = Login()
    l.login("MNF","Dobest")
