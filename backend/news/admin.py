from django.contrib import admin
from .models import *


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(News, NewsAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Author, AuthorAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(City, CityAdmin)
