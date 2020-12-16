from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import auth
# Create your views here.


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

    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')

def cria_receita(request):
    return render(request, 'usuarios/cria_receita.html')