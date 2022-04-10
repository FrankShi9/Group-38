from django.test import TestCase
from django.urls import reverse,resolve
from Area_38_app.views import login,register,forget,logout,SDChart,RFMChart,TSChart,chooseFunc,uploadfile,demand,rfm,xts

class TestUrls(TestCase):
    # 测试login链接能否正常显示
    def test_url_login(self):
        url_login = resolve('/login/')
        self.assertEquals(url_login.func,login)

    # 测试register链接能否正常显示
    def test_url_register(self):
        url_register = resolve('/register/')
        self.assertEquals(url_register.func,register)

    # 测试forget链接能否正常显示
    def test_url_forget(self):
        url_forget = resolve('/forget/')
        self.assertEquals(url_forget.func,forget)

    # 测试logout链接能否正常显示
    # def test_url_logout(self):
    #     url_logout = resolve('/logout/')
    #     self.assertEquals(url_logout.func,logout)

    # 测试SDChart链接能否正常显示
    def test_url_SDChart(self):
        url_SDChart = resolve('/SDChart/')
        self.assertEquals(url_SDChart.func,SDChart)

    # 测试RFMChart链接能否正常显示
    def test_url_RFMChart(self):
        url_RFMChart = resolve('/RFMChart/')
        self.assertEquals(url_RFMChart.func,RFMChart)

    # 测试TSChart链接能否正常显示
    def test_url_TSChart(self):
        url_TSChart = resolve('/TSChart/')
        self.assertEquals(url_TSChart.func, TSChart)

    # 测试uploadfile链接能否正常显示
    def test_url_uploadfile(self):
        url_uploadfile = resolve('/uploadfile/')
        self.assertEquals(url_uploadfile.func, uploadfile)

    # 测试demand链接能否正常显示
    def test_url_demand(self):
        url_demand = resolve('/demand/')
        self.assertEquals(url_demand.func, demand)

    # 测试rfm链接能否正常显示
    def test_url_rfm(self):
        url_rfm = resolve('/rfm/')
        self.assertEquals(url_rfm.func, rfm)

    # 测试xts链接能否正常显示
    def test_url_xts(self):
        url_xts = resolve('/xts/')
        self.assertEquals(url_xts.func, xts)




