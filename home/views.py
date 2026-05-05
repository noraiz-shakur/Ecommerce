from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Menu


# Create your views here.
def home(request):
    return render(request, "home/index.html")


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home/index.html", {"restaurants": restaurants})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    menus = Menu.objects.filter(restaurant_id=id)

    return render(
        request, "home/details.html", {"restaurant": restaurant, "menus": menus}
    )


def add_menu(request):
    restaurants = Restaurant.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        restaurant_id = request.POST.get("restaurant")

        restaurant = Restaurant.objects.get(id=restaurant_id)

        Menu.objects.create(restaurant=restaurant, name=name, price=price)

        return redirect("restaurant_list")

    return render(request, "home/add_menu.html", {"restaurants": restaurants})


def read_menu(request):
    menus = Menu.objects.all()


def edit_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == "POST":
        menu.name = request.POST["name"]
        menu.price = request.POST["price"]
        menu.save()

        return redirect("restaurant_list")

    return render(request, "home/edit_menu.html", {"menu": menu})


def delete_menu(request, id):
    menu = get_object_or_404(Menu, id=id)
    menu.delete()

    return redirect("restaurant_list")
