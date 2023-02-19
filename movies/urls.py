from django.urls import path
from .views import MoviesView, MoviesDetailViews


urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path('movies/<int:movie_id>/', MoviesDetailViews.as_view()),
]
