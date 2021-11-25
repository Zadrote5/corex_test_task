from django.urls import path
from .api_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'city', CityViewSet, basename='city')
router.register(r'country', CountryViewSet, basename='country')
urlpatterns = router.urls

