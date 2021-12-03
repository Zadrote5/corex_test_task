from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import *
from ..serializers import *

User = get_user_model()

class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CitySerializer
    queryset = City.objects.all()


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permissions = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return Response(self.get_serializer(request.user).data)
