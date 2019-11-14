from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('about')
    return render(request, 'about.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')


def temat1(request):
    print('temat1')
    return render(request, 'temat1.html')
