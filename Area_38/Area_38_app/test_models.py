from django.test import TestCase,Client
from django.urls import reverse,resolve
from Area_38_app.models import UserInfo
from django.contrib.auth.models import User

#django.test 继承 unittest
class TestModel(TestCase):
    def setUp(self) -> None:
        UserInfo.objects.create(email='Yongyin.Yang19@student.xjtlu.edu.cn',password='123456789')

    def test_model(self):
        user_info = UserInfo.objects.get(email='Yongyin.Yang19@student.xjtlu.edu.cn')
        self.assertEquals(user_info.email, 'Yongyin.Yang19@student.xjtlu.edu.cn')
        self.assertEquals(user_info.password, '123456789')

class TestLoginAction(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('login')
        UserInfo.objects.create(email='Yongyin.Yang19@student.xjtlu.edu.cn',password='123456789')

    def test_login_password_wrong(self):
        """邮箱正确密码错误"""
        test_data = {'email': 'Yongyin.Yang19@student.xjtlu.edu.cn', 'password': '123455678'}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_email_wrong(self):
        """邮箱错误密码正确"""
        test_data = {'email': 'Yongyin.Yang18@student.xjtlu.edu.cn', 'password': '123456789'}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_email_password_wrong(self):
        """邮箱错误密码错误"""
        test_data = {'email': 'Yongyin.Yang18@student.xjtlu.edu.cn', 'password': '123455678'}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_email_password_null(self):
        """邮箱密码为空"""
        test_data = {'email':'','password':''}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_email_null(self):
        """邮箱为空"""
        test_data = {'email':'','password':'123456789'}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_password_null(self):
        """密码为空"""
        test_data = {'email':'Yongyin.Yang19@student.xjtlu.edu.cn','password':''}
        response = self.client.post(self.login_url, data=test_data)
        self.assertTrue(response, 'Login failed')

    def test_login_action_success1(self):
        """登录成功(邮箱密码正确)"""
        test_data = {'email':'Yongyin.Yang19@student.xjtlu.edu.cn','password':'123456789'}
        response = self.client.post(self.login_url, data=test_data)
        self.assertEquals(response.status_code, 302)

class TestRegisterAction(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.register_url = reverse('register')
        UserInfo.objects.create(email='Yongyin.Yang19@student.xjtlu.edu.cn',password='123456789')

    def test_register_action_fail5(self):
        """邮箱已注册"""
        test_data = {'email': 'Yongyin.Yang19@student.xjtlu.edu.cn', 'password': '12345678'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertEquals(response.status_code, 200)

    def test_register_action_action_success6(self):
        """密码八位"""
        test_data = {'email': 'Yongyin.Yang18@student.xjtlu.edu.cn', 'password': '12345678'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertEquals(response.status_code, 302)

    def test_register_action_action_success2(self):
        """密码19位"""
        test_data = {'email': 'Yongyin.Yang18@student.xjtlu.edu.cn', 'password': '1234567890123456789'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertEquals(response.status_code, 302)

    def test_register_action_action_success4(self):
        """密码20位"""
        test_data = {'email': 'Yongyin.Yang18@student.xjtlu.edu.cn', 'password': '12345678901234567890'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertEquals(response.status_code, 302)

    def test_register_action_fail1(self):
        """密码只有七位"""
        test_data = {'email':'Yongyin.Yang18@student.xjtlu.edu.cn','password':'1234567'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertTrue(response.status_code, 200)

    def test_register_action_fail2(self):
        """密码21位"""
        test_data = {'email':'Yongyin.Yang18@student.xjtlu.edu.cn','password':'123456789012345678901'}
        response = self.client.post(self.register_url, data=test_data)
        self.assertTrue(response.status_code, 200)

    # def test_register_action_fail3(self):
    #     """邮箱格式不对1"""
    #     test_data = {'email':'Yongyin@','password':'123456789'}
    #     response = self.client.post(self.register_url, data=test_data)
    #     self.assertTrue(response, 'Login failed')
    #
    # def test_register_action_fail4(self):
    #     """邮箱格式不对2"""
    #     test_data = {'email':'Yongyin@.','password':'123456789'}
    #     response = self.client.post(self.register_url, data=test_data)
    #     self.assertTrue(response, 'Login failed')


















        




