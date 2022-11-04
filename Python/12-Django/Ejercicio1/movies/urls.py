from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('directors/', views.directors, name='directors'),
]

# app_name = 'directors'
# urlpatterns = [
#     path('', views.directors, name='directors'),
#     # ex: /directors/5/
#     # path('<int:director_id>/', views.detail, name='detail'),
# ]