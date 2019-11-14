from django.urls import path
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('temat1/', views.temat1, name='temat1'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
