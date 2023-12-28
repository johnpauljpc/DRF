from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.
def snippet_list(request):
    query_set = Snippet.objects.all()
    serializer = SnippetSerializer(query_set, many = True)
    data = serializer.data
    return JsonResponse(data, safe=False)


def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)

    except:
        return JsonResponse("Error: snippet does not exist!", safe=False)
    serializer = SnippetSerializer(snippet)
    data = serializer.data
    return JsonResponse(data, safe=False)