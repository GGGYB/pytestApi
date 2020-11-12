# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午10:14
# @Author  : WangJuan
# @File    : Assert.py


"""
封装Assert方法

"""
from common import log
from common import consts
import json


class Assertions:
    def __init__(self):
        self.log = log.MyLog()

    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            self.log.info("statusCode right, expected_code is %s, statusCode is %s " % (expected_code, code))
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body, body_msg, expected_msg):
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            self.log.info(
                "Response body msg == expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg,  body[body_msg]))
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg,  body[body_msg]))
            consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串,若输入为数组先将数组转换为字符串
        :param body:
        :param expected_msg:
        :return:
        """

        try:
            text = json.dumps(''.join(body), ensure_ascii=False)
            assert expected_msg in text
            self.log.info("Response body Does contain expected_msg, expected_msg is %s" % expected_msg)
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            consts.RESULT_LIST.append('fail')

            raise
    def assert_in_dict(self,body,expBody):
        """
        #body字典中是否包含子字典
        :param body:
        :param expBody:
        :return:
        """
        dict = set(body.items())
        subDict = set(expBody.items())
        try:
            if  subDict.issubset(dict):
                self.log.info(f"Response dict in bodyDict, Response dict {expBody}")
        except:
            self.log.info(f"Response dict not in bodyDict, Response dict {expBody}")

