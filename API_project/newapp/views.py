from django.shortcuts import render
import requests
# Create your views here.

def index_page(request):
    url = requests.get("https://dummyjson.com/recipes")
    tags= requests.get("https://dummyjson.com/recipes/tags").json()
    response = url.json()
    data = response["recipes"]
    context = {
        "data": data,
        "tags": tags,
    }
    return render(request, "index .html", context)

def recipes(request):
    return render(request, "recipes.html")

def databytags(request, tag):
    url = requests.get(f"https://dummyjson.com/recipes/tag/{tag}")
    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    response = url.json()
    data = response["recipes"]
    context = {
        "data": data,
        "tags": tags,
    }
    return render(request, "index .html", context)

