from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    restaurants= Restaurant.objects.all()
    content = {'categories' : categories,
               'restaurants' : restaurants}
    return render(request, 'shareRes/index.html', content)

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content)

def create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name) # 생성자  : 클래스 명(인수)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create category")
    
def delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id) # 데이터 불러올 때 : 클래스.objects.get(id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('categoryCreate'))

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/restaurantCreate.html', content)

def create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    title = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = title, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')