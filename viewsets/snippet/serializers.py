from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # owner = serializers.CharField(read_only = True)
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code','highlight', 'linenos', 'language', 'style', 'created', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # snippets = serializers.Hyperlink(url ="snippet-detail" ,obj=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']

    