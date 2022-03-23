from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from .models import User
from .serializer import LoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .models import UserInfo

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Area_38_app')

''' Backup code 
class LoginList(LoginRequiredMixin, APIView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def LoginList(self, request, format=None):
        loginKits = User.objects.all()[0:5]  # change table name
        serializer = LoginSerializer(loginKits, many=True)
        return Response(serializer.data)
'''


def login(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = models.UserInfo.objects.filter(email=email, password=password).first()
        if user_obj is not None:
            return HttpResponse('Login success, go to dashboard')
        else:
            return HttpResponse('Login failed')

    # TODO
    # if not user_obj:
    #     return redirect("/login/")  # Url redirect to login again
    # else:
    #     rep = redirect("/index/")  # Url redirect to index after success login
    #     rep.set_cookie("is_login", True)  # Update cookie
    #     return rep


def register(request):
    # if GET, simply render templates
    if request.method == "GET":
        print('we are here!')
        return render(request, "index.html")

    if request.method == "POST":
        userName = request.POST.get("userName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print('userName:', userName)
        print('email:', email)
        print('passwd:', password)
        user_obj = models.UserInfo.objects.filter(email=email, password=password).first()
        #user_obj = UserInfo(email=email, password=password)
        if user_obj is not None:
            print('register failed, user already exists')
            return HttpResponse('register failed, user already exists')

        else:
            user_obj = models.UserInfo.objects.create(email=email, password=password)
            user_obj.save()
            #logger.info(email)
            #logger.info(password)

            return redirect('/login')


def forget(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")


def SDChart(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")
