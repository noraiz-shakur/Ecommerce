from django.urls import path
from . import views

urlpatterns = [
    path("", views.restaurant_list, name="restaurant_list"),
    path("restaurant/<int:id>/", views.restaurant_detail, name="restaurant_detail"),
    path("add/", views.add_menu, name="add_menu"),
    path("edit/<int:id>/", views.edit_menu, name="edit_menu"),
    path("delete/<int:id>/", views.delete_menu, name="delete_menu"),
]
