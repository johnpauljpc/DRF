from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Snippet
from .serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list_create(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        data = request.data
        print("body   : ",data)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_rud(request, pk, format = None):
    try:
        snippet = Snippet.objects.get(pk=pk)
        serializer = SnippetSerializer(snippet)
    except:
        return Response("snippet not found!", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    
    if request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        snippet.delete()
        return Response(f"{snippet.title} deleted", status=status.HTTP_204_NO_CONTENT)