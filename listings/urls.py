from django.urls import path
from .import views

urlpatterns = [
    path('mainlistsingpage/',views.index,name = "mainlistsingpage"),
    path('<int:listing_id>',views.Listing,name = "singlelistpage"),
    path('search/',views.Search,name = "searchlistpage"),
]
