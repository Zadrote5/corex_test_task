from news.models import News, Author, City, Country
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country', 'id']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'id']


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField(max_length=1500)
    is_published = serializers.BooleanField(default=False)

    class Meta:
        model = News
        fields = ['title', 'author', 'content', 'is_published', 'cities', 'id']


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    email = serializers.EmailField()
    news_objects = News.objects.all()

    class Meta:
        model = Author
        fields = ['name', 'email', 'id']
