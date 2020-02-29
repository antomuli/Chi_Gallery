from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def my_photos(request):
    photos = Image.show_all_photos()
    locations = Location.objects.all()
    return render(request, 'all-photos/photos.html', {"photos":photos, "locations":locations})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_photos = Image.search_photo_by_category(category)
        locations = Location.objects.all()
        message = f"{category}"

        return render(request, 'all-photos/search.html', {"message":message, "photos":searched_photos, "locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})


def get_category(request, category):
    # category_results = category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(category__category_name = category)
    return render(request,'all-photos/photos.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request, location_name):
    category_results = category.objects.all()
    locations = Location.objects.all()
    location_result = Image.objects.filter(location__id= location_name)
    return render(request,'all-photos/locations.html',{'all_images':location_result,'category_results':category_results,'locations':locations})
