from django.db import models
from django.db.models import CASCADE


class Country(models.Model):
    name = models.TextField(max_length=250, verbose_name='Название страны')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class City(models.Model):
    name = models.TextField(max_length=250, verbose_name='Название города')
    country = models.ForeignKey(Country, on_delete=CASCADE, related_name='author', verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Author(models.Model):
    name = models.TextField(max_length=250, verbose_name='Имя автора')
    email = models.EmailField(max_length=250, verbose_name='Почта автора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class News(models.Model):
    title = models.TextField(max_length=250, verbose_name='Заголовок новости')
    author = models.ForeignKey(Author, on_delete=CASCADE, related_name='author', verbose_name='Автор новости')
    content = models.TextField(max_length=1500, verbose_name='Содержание новости')
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    cities = models.ManyToManyField(City, related_name='news', verbose_name='Города')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
