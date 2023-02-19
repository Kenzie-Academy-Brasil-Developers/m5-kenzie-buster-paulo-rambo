from rest_framework import serializers
from accounts.models import User
from .models import Movie


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
