from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Category, Reservation

# Create your views here.
def index(request, view_mode):
    data = Category.objects.all() 
    items = Item.objects.all()
    return render(request, 'manager/overview.html', {'categories' : data, 'view_mode' : view_mode, 'items' : items})

def category(request, category_id):
    data = Item.objects.filter(category__id=category_id)
    category_obj = Category.objects.get(id=category_id)
    return render(request, 'manager/category.html', {'items' : data, 'category' : category_obj})

def details(request, item_id):
    item = Item.objects.get(id=item_id)
    reservations = Reservation.objects.filter(item__id=item_id)
    curr_res = None
    if len(reservations) > 0:
        curr_res = reservations[0]
    return render(request, 'manager/details.html', {'item' : item, 'reservation' : curr_res})

def search(request):
    return HttpResponse("search result")
