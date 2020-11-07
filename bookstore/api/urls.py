from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "Codescaler BookStore Restful Web Service"
router.get_api_root_view().cls.__doc__ = "API to work with a virtual bookstore website"

router.register(r'api/books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
