from pylibs.login import Login
import requests
from common.Cfg import *
import json
class UserManage(object):
    def __init__(self,):

        pass
    def add_user(self,token,body):
        """
        :param baseUrl:
        :param body:
        :param expRet:
        :return:
        """
        url = HOST + "/api/v1/users"
        header = {
            "Authorization":token
        }
        res = requests.post(url,json = json.loads(body), headers = header)
        print(res.json())
        return res.json()
if __name__ == '__main__':
    l = Login()
    token = l.login("MNF","Dobest")["token"]
    user = UserManage()
    user.add_user("/api/v1/users",token)