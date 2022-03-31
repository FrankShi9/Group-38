from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('forget/', views.forget),
    path('SDChart/', views.SDChart),
    path('RFMChart/', views.RFMChart),
    path('TSChart/', views.TSChart),
    path('uploadfile/', views.uploadfile),
    path('chooseFunc/', views.chooseFunc),
    path('demand/', views.demand),
    path('rfm/', views.rfm),
    path('xts/', views.xts),
]