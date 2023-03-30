from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Custumer

# Create your views here.
def home(request):
    #
    customers = Custumer.objects.all()

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
        return render(request, "home.html", {'customers': customers})


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
    if request.is_authenticated:
        # Find the customer
        pass

