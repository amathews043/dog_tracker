from django.shortcuts import render
from .models import Household
from django.forms import modelform_factory

# Create your views here.

def home_page(request): 
    return render(request, "dog_tracker/home_page.html")

def create_household(request):
    HouseholdForm = modelform_factory(Household, fields=['name'])
    form = HouseholdForm()
    return render(request, "dog_tracker/create_household.html", {'form':form})