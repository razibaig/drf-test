from rest_framework.views import APIView

from .models import NewUser
from rest_framework import generics
from .serializers import UserSerializer, CreateUserSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response


class UserGetUpdateView(generics.ListAPIView, generics.UpdateAPIView):
    """
    API endpoint that shows user list and edit profile.
    """
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == "GET":
            if self.request.user.is_authenticated and self.request.user.is_staff:
                return CreateUserSerializer
            elif self.request.user.is_authenticated and self.request.user.is_staff is False:
                return UserSerializer
        elif self.request.method == "PATCH":
            if self.request.user.is_authenticated and self.request.user.is_staff:
                return CreateUserSerializer
            elif self.request.user.is_authenticated and self.request.user.is_staff is False:
                return UserSerializer

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):

        serializer = CreateUserSerializer(self.get_object(), request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CreateUserView(generics.ListCreateAPIView):

    queryset = NewUser.objects.all()
    serializer_class = CreateUserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        user = NewUser.objects.get(email=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)

