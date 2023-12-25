from django.urls import path, include
from rest_framework import routers


from .views import UserViewset, GroupViewset

router = routers.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r"group", GroupViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls"))
    

]

urlpatterns += router.urls