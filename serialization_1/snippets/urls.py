from django.urls import path
from . import views

urlpatterns=[
    path('', views.snippet_list, name="snippet-list"),
    path('<pk>/', views.snippet_detail),
]