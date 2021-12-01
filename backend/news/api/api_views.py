from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import *
from ..serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class NewsViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'list': NewsListSerializer
    }
    queryset = News.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, NewsSerializer)

    def perform_create(self, serializer):
        data = self.request.data
        author = data.get('author')
        author = Author.objects.filter(id=author).first()
        instance: News = serializer.save(author=author)
        cities = City.objects.filter(id__in=data.get('cities'))
        instance.cities.set(cities)

    def perform_update(self, serializer):
        data = self.request.data
        author = data.get('author')
        author = Author.objects.filter(id=author).first()
        instance: News = serializer.save(author=author)
        cities = City.objects.filter(id__in=data.get('cities'))
        instance.cities.set(cities)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
