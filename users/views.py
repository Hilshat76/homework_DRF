from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class ProfileAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
