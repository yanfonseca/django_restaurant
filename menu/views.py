from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

def search(request):
    print(request)

    recipes = Recipe.objects.order_by('-created_at').filter(publish=True)

    if 'xxsearch' in request.GET:
        print('passou 1')
        search_filter = request.GET['xxsearch']

        print(search)
        # if 'xxsearch':
        print('passou 2')
        recipes = recipes.filter(name__icontains=search_filter)

    context = {
        'recipes':recipes
    }
    
    return render(request, 'buscar.html', context)


def home(request):

    # recipes = Recipe.objects.all()
    
    recipes = Recipe.objects.order_by('-created_at').filter(publish=True)
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
