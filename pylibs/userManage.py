from pylibs.login import Login
import requests
from common.cfg import *
import json
from common import getData
class UserManage(object):
    def __init__(self,):

        pass
    def add_user(self,token,url,body):
        """
        :param baseUrl:
        :param body:
        :param expRet:
        :return:
        """
        baseurl = HOST + url
        # print(url)
        header = {
            "Authorization":token
        }
        res = requests.post(baseurl,json = json.loads(body), headers = header)
        # print(res.json())
        return res.json()
if __name__ == '__main__':
    l = Login()
    token = l.login("MNF","Dobest")["token"]
    user = UserManage()
    data = getData.get_excel_data("user",2,3,4,7,8)
    print(data)
    user.add_user(token,"/api/v1/users",data[0][2])