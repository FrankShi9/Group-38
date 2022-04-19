from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login),
    path('register/', views.register),
    path('forget/', views.forget),
    path('SDChart/', views.SDChart),
    path('RFMChart/', views.RFMChart),
    path('TSChart/', views.TSChart),
    path('uploadfile/', views.uploadfile),
    #path('chooseFunc/', views.chooseFunc),
    path('home/', views.home),
    path('demand/', views.demand),
    path('rfm/', views.rfm),
    path('xts/', views.xts),
    path('logout/',views.logout),
    path('hw/', views.holt_winters),
    path('AboutUs/', views.AboutUs),
    path('Guidance/', views.Guidance),
    path('Admin/', views.Admin),
    path('pdf_download/', views.pdf_download),
    path('history/', views.history),
    path('history/api/', views.history_api),
]