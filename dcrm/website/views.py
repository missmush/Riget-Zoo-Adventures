from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'website/about.html')

def zoobooking(request):
    return render(request,'website/zoobooking.html')

def hotelbooking(request):
    return render(request,'website/hotelbooking.html')

def adopt(request):
    return render(request,'website/adopt.html')