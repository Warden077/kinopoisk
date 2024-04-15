from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'Tea/home.html',{'movies': movies})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'Tea/list/movie_list.html',{'movies': movies})

def movie_detail(request, movie_id):
    return render(request, 'Tea/detail/movie_detail.html')

def actor_detail(request, actor_id):
    return render(request, 'Tea/detail/actor_detail.html')

def actor_list(request):
    return render(request, 'Tea/list/actor_list.html')

def producer_detail(request, producer_id):
    return render(request, 'Tea/detail/producer_detail.html')

def producer_list(request):
    return render(request, 'Tea/list/producer_list.html')

def director_detail(request, director_id):
    return render(request, 'Tea/detail/director_detail.html')

def director_list(request):
    return render(request, 'Tea/list/director_list.html')

def genres_detail(request, genres_id):
    return render(request, 'Tea/detail/genres_detail.html')

def genres_list(request):
    return render(request, 'Tea/list/genresr_list.html')