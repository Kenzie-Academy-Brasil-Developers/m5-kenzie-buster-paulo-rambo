from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from .permissions import MoviesPermission, MoviesDetailsPermission
from .models import Movie


class MoviesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviesPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(owner_id=request.user.id)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MoviesDetailViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviesDetailsPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()
        return Response(status=status.HTTP_201_CREATED)
