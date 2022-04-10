from django.test import TestCase,Client
from django.urls import reverse,resolve
from Area_38_app.models import UserInfo
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from datetime import timedelta

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.login_url=reverse('login')
        self.register_url = reverse('register')
        self.forget_url = reverse('forget')
        self.SDChart_url = reverse('SDChart')
        self.RFMChart_url = reverse('RFMChart')
        self.TSChart_url = reverse('TSChart')
        self.uploadfile_url = reverse('uploadfile')
        self.chooseFunc_url = reverse('chooseFunc')
        self.demand_url = reverse('demand')
        self.rfm_url = reverse('rfm')
        self.xts_url = reverse('xts')
    # 测试login成功响应码
    def test_login_GET1(self):
        response= self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
    # 测试register成功响应码
    def test_register_GET1(self):
        response= self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
    # 测试forget成功响应码
    def test_forget_GET1(self):
        response= self.client.get(self.forget_url)
        self.assertEquals(response.status_code, 200)
    # 测试SDChart成功响应码
    def test_SDChart_GET1(self):
        response= self.client.get(self.SDChart_url)
        self.assertEquals(response.status_code, 200)
    # 测试RFMChart成功响应码
    def test_RFMChart_GET1(self):
        response= self.client.get(self.RFMChart_url)
        self.assertEquals(response.status_code, 200)
    # 测试TSChart成功响应码
    def test_TSChart_GET1(self):
        response= self.client.get(self.TSChart_url)
        self.assertEquals(response.status_code, 200)
    # 测试uploadfile成功响应码
    def test_uploadfile_GET1(self):
        response= self.client.get(self.forget_url)
        self.assertEquals(response.status_code, 200)
    # 测试chooseFunc成功响应码
    def test_chooseFunc_GET1(self):
        response= self.client.get(self.chooseFunc_url)
        self.assertEquals(response.status_code, 200)


    # 用于检查响应是使用哪个模板渲染（注意，这个方法只能测试通过测试客户端获取的响应）
    def test_login_GET2(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_GET2(self):
        response= self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_forget_GET2(self):
        response = self.client.get(self.forget_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_SDChart_GET2(self):
        response = self.client.get(self.SDChart_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_RFMChart_GET2(self):
        response = self.client.get(self.RFMChart_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_TSChart_GET2(self):
        response = self.client.get(self.TSChart_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_uploadfile_GET2(self):
        response = self.client.get(self.uploadfile_url)
        self.assertTemplateUsed(response, 'index.html')

    def test_chooseFunc_GET2(self):
        response = self.client.get(self.chooseFunc_url)
        self.assertTemplateUsed(response, 'index.html')


    #POST接口测试
    def test_login_POST_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEquals(response.status_code,200)

    def test_register_POST_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code,302)

    def test_register_POST_add_new_data(self):
        UserInfo.objects.create(email='Yongyin.Yang19@student.xjtlu.edu.cn', password='123455678')
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(UserInfo.objects.first().email,'Yongyin.Yang19@student.xjtlu.edu.cn')

    def test_uploadfile_POST_no_data(self):
        response = self.client.post(self.uploadfile_url)
        self.assertEquals(response.status_code,200)














