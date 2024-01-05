from django.shortcuts import render, get_object_or_404
from rest_framework import mixins, generics, permissions, status
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.response import Response

from rest_framework.reverse import reverse
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.views import APIView
from rest_framework import viewsets


# local imports
from .serializers import SnippetSerializer, User, UserSerializer
from .models import Snippet
from .permissions import IsOwnerOrReadOnly, IsUserOrReadOnly

# Create your views here.

class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
   


