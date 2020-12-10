from django.contrib import admin

from .models import Recipe
# Register your models here.


class ListRecipe(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'preparation_time')

    list_display_links = ('id', 'name')


admin.site.register(Recipe, ListRecipe)