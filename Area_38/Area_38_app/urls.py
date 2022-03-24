from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('forget/', views.forget),
    path('SDChart/', views.SDChart),
    path('uploadfile/', views.uploadfile),
]