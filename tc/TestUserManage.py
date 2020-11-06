from pylibs.UserManage import UserManage
from pylibs.Login import Login
from common.GetData import get_excel_data
from common.Assert import  Assertions
from common.Consts import *

import allure
import pytest
import os
class TestUserManage(object):
    def setup_class(self):
        self.token = Login().login("MNF","Dobest")["token"]
        self.test = Assertions()
    @allure.title("新增用户")
    @pytest.mark.parametrize("inData,exp",get_excel_data("user",2,6,7,8))
    def test_add_user(self,inData,exp):
        res = UserManage().add_user(self.token,inData)
        print(inData)
        assert self.test.assert_code(res["code"],500)
        print(res)

if __name__ == '__main__':

    pytest.main(['TestUserManage.py', '-s','--alluredir', '../report/tmp'])
    # os.system('allure generate report/ -o ../report/report')
    os.system('allure generate  ../report/tmp -o ../report/tmp --clean')
