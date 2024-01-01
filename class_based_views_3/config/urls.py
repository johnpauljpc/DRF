
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.SnippetList.as_view()),
    path("mx/", views.SnippetListMixin.as_view()),
    path("gn/", views.SnippetListGN.as_view()),
    path("<pk>/", views.Rud.as_view()),
    path("mx/<pk>/", views.RudMx.as_view()),
    path("gn/<pk>/", views.RudGN.as_view()),

   
]
urlpatterns = format_suffix_patterns(urlpatterns)