from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from api import views

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, basename='userView')
router.register(r'messages', views.MessageViewSet, basename='messageView')

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
