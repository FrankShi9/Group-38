from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Area_38_app.urls')), # demo add
    path('', TemplateView.as_view(template_name='index.html'))
]
