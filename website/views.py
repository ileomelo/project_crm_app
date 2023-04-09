from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Customer

# Create your views here.
def home(request):
    #
    customers = Customer.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Você foi logado com sucesso!")
            return redirect("home")

        else:
            messages.success(request, "OPS! Aconteceu um erro, tente novamente!")
            return redirect("home")
    else:
        return render(request, "home.html", {"customers": customers})


def logout_user(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registrado com sucesso! Bem vindo!!")

            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def get_customer(request, pk):
    if request.user.is_authenticated:
        # Find the customer
        customer = Customer.objects.get(id=pk)

        return render(request, "customer.html", {"customer": customer})
    else:
        messages.info(request, "Você precisa estar logado para acessar esta pagina!!")
        return redirect("home")


def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deletado com sucesso!!")
        return redirect("home")
    else:
        messages.success(request, "Você precisa estar logado para fazer modificações!!")
        return redirect("home")


def new_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Cliente adicionado com sucesso!!")
                return redirect("home")
        return render(request, "new_customer.html", {'form':form})
    else:
        messages.success(request, "Para acessar esta pagina, faça o login")
        return redirect('home')
