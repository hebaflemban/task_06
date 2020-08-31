from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    new_restaurant = RestaurantForm()
    if request.method == 'POST' :
        new_restaurant = RestaurantForm(request.POST)
        #if new_restaurant.is_valid():
        new_restaurant.save()
        return redirect('restaurant-list')
    context = {
        'form' : new_restaurant
        #var used in html

    }
    return render(request, 'create.html', context)
