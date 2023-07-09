from django.shortcuts import render, redirect
from .models import Household
from django.forms import modelform_factory

# Create your views here.

def home_page(request): 
    return render(request, "dog_tracker/home_page.html")

def create_household(request):
    HouseholdForm = modelform_factory(Household, fields=['name'])
    if request.method == "GET":
        form = HouseholdForm()
        return render(request, "dog_tracker/create_household.html", {'form':form})
    else: 
        form = HouseholdForm(request.POST)
        if form.is_valid(): 
            household = form.save()
            household.owners.add(request.user)
            return redirect('detail_household', id=household.id)
        else: 
            return render(request, "dog_tracker/create_household.html", {'form':form})

def detail_household(request,id):
    household = Household.objects.get(id=id)
    return render(request, "dog_tracker/detail_household.html", {"household": household})

def list_household(request): 
    households = Household.objects.all()
    return render(request, "dog_tracker/list_household.html", {"households": households})
