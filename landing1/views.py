from django.shortcuts import render

# Create your views here.
def index(request):
    return render('landing1',"Hello, world. You're at landing1 index.")