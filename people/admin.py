from django.contrib import admin

# Register your models here.

from .models import PeopleModel


class ListPeople(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_per_page = 10

admin.site.register(PeopleModel, ListPeople)
