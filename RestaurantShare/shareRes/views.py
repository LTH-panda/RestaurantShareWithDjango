from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/index.html', content)

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content)

def create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create category")

def create_restaurant(request):
    return render(request, 'shareRes/restaurantCreate.html')

def detail_restaurant(request):
    return render(request, 'shareRes/restaurantDetail.html')