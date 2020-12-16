from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib import auth
# Create your views here.

from menu.models import Recipe


def subscribe(request):

    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        print(nome, email, senha, senha2)
        print('request', request)
        print(request.headers)

        if not nome.strip():
            print('Escreva um nome valido')
            return redirect('cadastro')

        if not email.strip():
            print('Escreva um email valido')
            return redirect('cadastro')
        
        if senha != senha2:
            print('Senhas diferentes')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuario já foi cadastrado anteriormente.')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        

        print('Usuário cadastrado com sucesso')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print(email, senha)
            print("Os campos email e senha não podem ficar em branco")
            return redirect('login')

        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            print(nome)

            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def dashboard(request):
    print('############')
    if request.user.is_authenticated:
        print('aaaaaaaaaaaaaaa')

        receitas = Recipe.objects.order_by('-created_at').filter(person=request.user.id)

        context = {
            'recipes':receitas
        }

        return render(request, 'usuarios/dashboard.html', context)
    else:
        print('############')
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')

def cria_receita(request):

    if request.method == "POST":
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']

        user = get_object_or_404(User, pk=request.user.id)
        print(user, nome_receita,
              ingredientes,
              modo_preparo,
              tempo_preparo,
              rendimento,
              categoria,
              foto_receita)
        receita = Recipe.objects.create(person=user,
                                        name=nome_receita,
                                        ingredient=ingredientes,
                                        preparation=modo_preparo,
                                        preparation_time=tempo_preparo,
                                        portions=rendimento,
                                        category = categoria,
                                        photo_recipe=foto_receita )

        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')