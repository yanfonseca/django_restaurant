from django.shortcuts import render, redirect

from django.contrib.auth.models import User

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
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass

