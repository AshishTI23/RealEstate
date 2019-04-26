from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.HomePage, name = 'Homepage'),
    path('about/',views.About,name = 'about'),
]
