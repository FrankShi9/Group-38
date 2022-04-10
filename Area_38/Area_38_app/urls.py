from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('forget/', views.forget,name='forget'),
    path('SDChart/', views.SDChart,name='SDChart'),
    path('RFMChart/', views.RFMChart,name='RFMChart'),
    path('TSChart/', views.TSChart,name='TSChart'),
    path('uploadfile/', views.uploadfile,name='uploadfile'),
    path('chooseFunc/', views.chooseFunc,name='chooseFunc'),
    path('demand/', views.demand,name='demand'),
    path('rfm/', views.rfm,name='rfm'),
    path('xts/', views.xts,name='xts'),
]
