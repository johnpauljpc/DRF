from django.shortcuts import render
from rest_framework import mixins, generics, permissions, response, status

# local imports
from .serializers import SnippetSerializer, User, UserSerializer
from .models import Snippet
from .permissions import IsOwnerOrReadOnly, IsUserOrReadOnly

# Create your views here.
# USING GENERIC CLASS BASED VIEWS
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class Rud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly]



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserRud(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    def perform_update(self, serializer):
        if serializer.instance.username != self.request.user.username:
            return False

        return super().perform_update(serializer)