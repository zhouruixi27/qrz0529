# -*- coding: utf-8 -*-
import requests
import unittest

# http统一处理
# 使用libs封装requests的传参方式，尽可能的省略传参方法
class BaseHttp(object):
    host = 'http://localhost'
    def post_data(self,url,data,icon=1,*args,**kwargs):
        '''
        :param url:
        :param data:
        :param icon: 1代表正常请求，2代表文件上传
        :return:
        '''
        url = '{}{}'.format(self.host,url)
        if icon == 1:
            result = requests.post(url=url,data=data,*args,**kwargs)
        elif icon ==  2 :
            result = requests.post(url=url,files=data,*args,**kwargs)
        return result


    def get_data(self,url,params,*args,**kwargs):
        '''
        :param url:
        :param params:
        :return:
        '''
        result = requests.get(url=url,params=params,*args,**kwargs)
        return result
class verifyClass(unittest.TestCase):
    #校验状态码
    def verifycode(self,status_code,v_code):
        '''
        :param status_code: 响应状态码
        :param v_code:
        :return:
        '''
        self.assertEqual(result.status_code, v_code)
    def verifyjson(self,result,key,value):
        '''
        :param result:
        :param key:
        :param value:
        :return:
        '''
        result = result.json()
        v = result.get(key)
        self.asserEqual(v,value)
    def verifyHtml(self, result,value):
        '''
        :param result:
        :param value:
        :return:
        '''
        result = result.text
        self.asserAlmostEqual(result,value)
