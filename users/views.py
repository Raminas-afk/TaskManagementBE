from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserRegistrationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.create_new_user(serializer.validated_data)
            return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    