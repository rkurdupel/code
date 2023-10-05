from django.urls import path
from .views import home_page, register_page, login_page

urlpatterns = [
    path('', home_page, name = "home_page"),
    path('register/', register_page, name = "register_page"),
    path('login/', login_page, name = "login_page") # in html functions are looked from name argument name = "login_page"
]   