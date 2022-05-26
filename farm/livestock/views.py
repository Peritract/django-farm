from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Animal

# Create your views here.

def index(request):

    return HttpResponse("""
    <h1>Livestock</h1>
    <i>Where animals are things</i>
    """)

def about(request):

    return HttpResponse("""
    <h1>About</h1>
    <p>Sunset Oaks Farm is a happy community of independently-minded cows.</p>
    """)

def cows(request):

    data = {
        "cows": Animal.objects.filter(species=4)
    }

    return render(request, 'cows.html', data)

def cow(request, id):

    data = {
        "cow": get_object_or_404(Animal, pk=id)
    }

    return render(request, 'cow.html', data)

def list_cows(request):

    data = {
        # for each animal in the list of animals (from the database)
        # Convert it into a dictionary
        # Put the dictionary into a list

        # cows = []
        # for animal in Animal.objects.filter(species=4):
        #    cows.append(animal.to_dict())
        "cows": [animal.to_dict() for animal in Animal.objects.filter(species=4)],
        "alligators": []
    }

    return JsonResponse(data)

def not_found_404(request, exception):
    return render(request, '404.html')