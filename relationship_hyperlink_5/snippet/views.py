from django.shortcuts import render, get_object_or_404
from rest_framework import mixins, generics, permissions, response, status
from rest_framework.decorators import api_view, renderer_classes

from rest_framework.reverse import reverse
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.views import APIView


# local imports
from .serializers import SnippetSerializer, User, UserSerializer
from .models import Snippet
from .permissions import IsOwnerOrReadOnly, IsUserOrReadOnly

# Create your views here.

# Creating an endpoint for the root of our API
@api_view(["GET"])
def api_root(request, format =None):
    return response.Response({
        "SNIPPETS": reverse('snippet-list', request=request, format=format),
        "USERS": reverse('user-list', request=request, format=format)
    })

    

@api_view(['GET'])
def snippet_user_objects(request, format=None):
    snippets = Snippet.objects.all()
    users = User.objects.all()
    serializer1 = SnippetSerializer(snippets, many = True, context = {"request": request})
    serializer2 = UserSerializer(users, many = True,  context = {"request": request})
    return response.Response(
        {
            'SNIPPETS': serializer1.data,
            'USERS': serializer2.data
        }
    )



class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [StaticHTMLRenderer]

    def get(self, request, *args,**kwargs):
        snippet = self.get_object()
        return response.Response(snippet.highlighted)
    

# class SnippetHighlight(APIView):
#     renderer_classes = [StaticHTMLRenderer]

#     def get(self, request, pk):
#         snippet = get_object_or_404(Snippet, pk=pk)
#         return response.Response(snippet.highlighted)

# USING GENERIC CLASS BASED VIEWS
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly]



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    def perform_update(self, serializer):
        if serializer.instance.username != self.request.user.username:
            return False

        return super().perform_update(serializer)
    


