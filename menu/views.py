from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

def home(request):

    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request,'index.html', context)

def receita(request, receita_id):
    recipe = get_object_or_404(Recipe, pk = receita_id)

    context ={
        'recipe': recipe
    }

    return render(request, 'receita.html', context)

# You can use this code if you don't have a database created with postgresql

# def home(request):

#     recipes = {
#         1:'Lasanha',
#         2: 'Sopa de Legumes',
#         3: 'Sorvete',
#         4: 'Bolo de chocolate'
#         }

#     context = {
#         'recipe_names': recipes
#     }

#     return render(request,'index.html', context)
