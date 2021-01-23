from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantCreate/', views.restaurantCreate, name = 'restaurantCreate'),
    path('restaurantCreate/create', views.create_restaurant, name = 'create_restaurant'),
    path('restaurantDetail/delete', views.delete_restaurant, name = 'delete_restaurant'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name = 'restaurantDetail'),
    path('restaurantDetail/updatePage/update',views.update_restaurant, name = 'update_restaurant'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name = 'restaurantUpdate'),
    path('categoryCreate/', views.categoryCreate, name = 'categoryCreate'),
    path('categoryCreate/create', views.create_category, name = 'create_category'),
    path('categoryCreate/delete', views.delete_category, name = 'delete_category'),
    
]