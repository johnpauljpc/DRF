from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from django.http import Http404, HttpResponse

# local imports
from .serializers import SnippetSerializer
from .models import Snippet

# Create your views here.

# USING CLASS BASED VIEWS
class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        data = request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Rud(APIView):
    def get_object(self,  pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        snippet = self.get_object(pk)
        data = request.data
        serializer = SnippetSerializer(snippet, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response("deleted", status=status.HTTP_204_NO_CONTENT)
    

# USING MIXINS 
class SnippetListMixin(mixins.ListModelMixin, 
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RudMx(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
            mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# USING GENERIC CLASS BASED VIEWS
class SnippetListGN(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class RudGN(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
