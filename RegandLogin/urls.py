from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegister,name = "register"),
    path('Login/',views.UserLogin,name = "login"),
    path('Logout/',views.UserLogout,name = "logoutview"),
    path('dashbord/',views.Dashbord,name = "dashbord"),
]
