from pylibs.userManage import UserManage
from pylibs.login import Login
from common import getData
from common.myAssert import  Assertions
from common.consts import *
import json

import allure
import pytest
import os
class TestUserManage(object):
    def setup_class(self):
        self.token = Login().login("MNF","Dobest")["token"]
        self.test = Assertions()
    @allure.title("新增用户")
    @pytest.mark.parametrize("url,body,exp",getData.get_excel_data("user",2,6,4,7,8))
    def test_add_user(self,url,body,exp):
        res = UserManage().add_user(self.token,url,body)
        assert self.test.assert_code(res["code"],json.loads(exp)["code"])
    @pytest.mark.parametrize("caseID,url,body,exp",getData.get_db_data("../data/user","user"))
    def test_add_user01(self,caseID,url,body,exp):
        res = UserManage().add_user(self.token,url,body)
        assert self.test.assert_code(res["code"],json.loads(exp)["code"])

if __name__ == '__main__':
    pytest.main(['test_UserManage.py', '-s','--alluredir', '../report/tmp'])
    # os.system('allure generate report/ -o ../report/report')
    os.system('allure generate  ../report/tmp -o ../report/tmp --clean')
