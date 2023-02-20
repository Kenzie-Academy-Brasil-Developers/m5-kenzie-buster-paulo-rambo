from rest_framework import serializers
from accounts.models import User
from .models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(max_length=150, allow_null=True, default=None)
    rating = serializers.CharField(max_length=20, allow_null=True)
    duration = serializers.CharField(allow_null=True)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj: Movie) -> str:
        user = User.objects.get(id=obj.owner_id)
        return user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder) -> str:
        movie = Movie.objects.get(id=obj.movie_id)
        return movie.title

    def get_buyed_by(self, obj: MovieOrder) -> str:
        user = User.objects.get(id=obj.user_id)
        return user.email

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
