from django.shortcuts import render, redirect

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

        print('deu certo')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass

