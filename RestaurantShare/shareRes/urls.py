from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantCreate/', views.restaurantCreate, name = 'restaurantCreate'),
    path('restaurantCreate/create', views.create_restaurant, name = 'create_restaurant'),
    path('restaurantDetail/', views.restaurantDetail, name = 'restaurantDetail'),
    path('categoryCreate/', views.categoryCreate, name = 'categoryCreate'),
    path('categoryCreate/create', views.create_category, name = 'create_category'),
    path('categoryCreate/delete', views.delete_category, name = 'delete_category'),
    
]