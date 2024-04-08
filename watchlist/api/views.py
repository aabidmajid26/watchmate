from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        if not movie:
            return Response(serializer.errors)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)