from django.urls import path
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('temat1/index.html/', views.home, name='home'),
    path('temat2/index.html/', views.home, name='home'),
    path('temat3/index.html/', views.home, name='home'),
    path('temat4/index.html/', views.home, name='home'),
    path('temat1/', views.temat1, name='temat1'),
    path('temat2/', views.temat2, name='temat2'),
    path('temat3/', views.temat3, name='temat3'),
    path('temat4/', views.temat4, name='temat4'),

]
