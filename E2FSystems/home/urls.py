
from django.contrib import admin
from django.urls import include, re_path,path

from home.views import admin_login, contact_us, download_data, home,add_program,result,search

urlpatterns = [
    path('', home),
    path('result/',result),
    path('admin_login/',admin_login),
    path('add_program/',add_program),
    path('contact_us/',contact_us),
    path('search/',search),
    path('download_data/',download_data),

]
