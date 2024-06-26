from django.contrib import admin
from django.urls import path, include

# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAV.as_view(), name='movie-details')
    # path('<int:pk>/', movie_details, name='movie-details')
]
