from django.contrib import admin
from .models import Snippet
# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    # fields = ['title', 'code', 'linenos', 'language', 'style']
    list_display =['id', 'title', 'code', 'linenos', 'language', 'style', 'created']


admin.site.register(Snippet, SnippetAdmin)