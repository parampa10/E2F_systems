from django.contrib import admin
from django.urls import include, re_path,path

from home.views import admin_login, home,add_program,result

urlpatterns = [
    path('', home),
    path('result/',result),
    path('admin_login/',admin_login),
    path('add_program/',add_program),
]
