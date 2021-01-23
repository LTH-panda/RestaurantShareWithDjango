from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantCreate/', views.create_restaurant, name = 'create_restaurant'),
    path('restaurantDetail/', views.detail_restaurant, name = 'detail_restaurant'),
    path('categoryCreate/', views.categoryCreate, name = 'categoryCreate'),
    path('categoryCreate/create', views.create_category, name = 'create_category'),
    
]