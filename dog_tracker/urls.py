from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('households/create/', views.create_household, name='create_household'),
]