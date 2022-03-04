from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializer import LoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


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

    # if request.method == "POST"    
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    # TODO
    # if not user_obj:
    #     return redirect("/login/")  # Url redirect to login again
    # else:
    #     rep = redirect("/index/")  # Url redirect to index after success login
    #     rep.set_cookie("is_login", True)  # Update cookie
    #     return rep
