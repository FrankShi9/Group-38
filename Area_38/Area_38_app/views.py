import os

from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
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
            response = HttpResponse('Login success, go to dashboard')
            response.set_cookie("is_login", True, max_age=60*60*24)
            response.set_cookie("email", email, max_age=60*60*24)
            return response
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

def logout(request):
    response = redirect('/login/')
    response.delete_cookie("is_login")
    response.delete_cookie("email")
    return

def SDChart(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")

def uploadfile(request):
    # if GET, simply render templates
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        file = request.FILES.get('file')
        if not file:
            print("no file")
            return HttpResponse("file not found")
        status = request.COOKIES.get('is_login')
        print(request.COOKIES)
        if status == "True":
            print("already login")
            user_email = request.COOKIES.get("email")
        else:
            print("didn't login")
            return HttpResponse("login required")
        uploadfilepath = "./"+user_email+"/upload"
        if not os.path.exists(uploadfilepath):
            os.makedirs(uploadfilepath)
        position = os.path.join(uploadfilepath, file.name)
        storage = open(position, 'wb')
        for chunk in file.chunks():
            storage.write(chunk)
        storage.close()
        return HttpResponse("file uploaded")