from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UsersView(APIView):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UsersLoginView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
