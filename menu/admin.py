from django.contrib import admin

from .models import Recipe
# Register your models here.


class ListRecipe(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'preparation_time', 'publish')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_filter = ('category',)

    list_per_page = 2

    list_editable = ('publish',)


admin.site.register(Recipe, ListRecipe)