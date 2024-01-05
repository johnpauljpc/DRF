from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("users", viewset=views.UserViewset, basename="user")
router.register(prefix="snippet", viewset=views.SnippetViewset, basename="snippet")

urlpatterns = [
    path("", include(router.urls))
]