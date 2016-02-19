from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    data = Item.objects.all() 
    return render(request, 'manager/main.html', {'items' : data})

def search(request):
    return HttpResponse("search result")
