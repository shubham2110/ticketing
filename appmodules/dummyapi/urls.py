from rest_framework import routers
from django.urls import path
from .views import Authenticate

router = routers.SimpleRouter()
#router.register(r'users', TestUserSet)

urlpatterns = [
    path('authenticate/', Authenticate),
]

urlpatterns += router.urls