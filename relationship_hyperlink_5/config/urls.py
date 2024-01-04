
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from rest_framework.urlpatterns import format_suffix_patterns
 

from snippet import views

urlpatterns = [
    path('', views.api_root),
    path("all/", views.snippet_user_objects),

    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),

    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path("users/", views.UserList.as_view(), name = "user-list"),
    path("users/<pk>/", views.UserDetail.as_view(), name = "user-detail"),
    path("snippet/<pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)