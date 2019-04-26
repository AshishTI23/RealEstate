from django.shortcuts import render
from listings.models import Listing as lst
from realtors.models import Realtor as rltr
from listings.choices import bedroom_choices,price_choices,state_choices
# Create your views here.
def HomePage(request):
    list = lst.objects.order_by('-list_date')[0:3]
    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings' : list,
    }
    return render(request,'testapp/homepage.html',context)

def About(request):
    #get all realtors
    realtors_all = rltr.objects.order_by('-hire_date')
    #get mvp
    realtors_mvp = rltr.objects.all().filter(is_mvp = True)

    context = {'realtors' : realtors_all,'mvp_realtors' : realtors_mvp,}

    return render(request,'testapp/about.html',context)
