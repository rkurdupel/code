# Create your views here.
from django.shortcuts import render
from .models import CustomUserManager

def home_page(request):
    return render(request, 'home_page.html')
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        middle_name = request.POST.get("middle_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        CustomUserManager.create_user(email, password, first_name, middle_name, last_name)

    return render(request, "register_page.html")
def login_page(request):
    return render(request, 'login_page.html')

def login_user(request):
    if request.method == "POST":
        return render(request, "home.html")
    return render(request, 'login.html')

