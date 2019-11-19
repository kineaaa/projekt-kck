from django.shortcuts import render
from django.core.files.storage import FileSystemStorage



def home(request):
    print('Home')
    return render(request, 'home.html')


def temat2(request):
    print('temat2')
    return render(request, 'temat2.html')

def temat3(request):
    print('temat3')
    return render(request, 'temat4.html')


def temat4(request):
    print('temat4')
    return render(request, 'temat3.html')


def temat1(request):
    print('temat1')
    return render(request, 'temat1.html')
