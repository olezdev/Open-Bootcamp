from django.shortcuts import render

from django.http import HttpResponse

from .models import Director, Movie

# def index(request):
#     return HttpResponse("Movies index.")

# atajo render
def index(request):
    latest_movie_list = Movie.objects.order_by('-year')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'movies/index.html', context)

def directors(request):
    latest_director_list = Director.objects.order_by('-first_name')[:5]
    context = {'latest_director_list': latest_director_list}
    return render(request, 'movies/directors.html', context)