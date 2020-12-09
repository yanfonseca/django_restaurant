from django.shortcuts import render

# Create your views here.

def home(request):

    recipes = {
        1:'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete',
        4: 'Bolo de chocolate'
        }

    context = {
        'recipe_names': recipes
    }

    return render(request,'index.html', context)

def receita(request):
    return render(request, 'receita.html')