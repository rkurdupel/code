# Create your views here.
from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')
def register_page(request):
    if request.method == "POST":
        return render(request, "home_page.html")
    return render(request, "register_page.html")
def login_page(request):
    return render(request, 'login_page.html')

def login_user(request):
    if request.method == "POST":
        return render(request, "home.html")
    return render(request, 'login.html')

