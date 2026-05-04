from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu


# Create your views here.
def home(request):
    return render(request, "home/index.html")

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home/index.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    menus = Menu.objects.filter(restaurant_id=id)

    return render(request, 'home/details.html', {
        'restaurant': restaurant,
        'menus': menus
    })


