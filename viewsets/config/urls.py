
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from rest_framework.urlpatterns import format_suffix_patterns
 

from snippet import views

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path("", include("snippet.urls")),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)