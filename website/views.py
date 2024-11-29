from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, Hotel_Booking_Form
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

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

def login(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    context = {'login_form': form}
    return render(request,'website/login.html', context=context)
    
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request,'website/register.html', context=context)

def hotel(request):

    form = Hotel_Booking_Form()

    if request.method == "POST":
        updated_request = request.POST.copy()
        updated_request.update({'hotel_user_id_id': request.user})

        form = Hotel_Booking_Form(updated_request)
