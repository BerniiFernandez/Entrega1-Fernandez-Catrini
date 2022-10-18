from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "index.html")

def loginchat(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST["username"]
            password=request.POST["password"]
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "chathome.html", {'message':f"Bienvenido {user}"})
            else:
                return render(request, "loginchat.html", {'formulario':form, 'mensaje':"Usuario o contraseña incorrectos"})
        else:
            return render(request, "loginchat.html", {'formulario':form, "mensaje":"Usuario o contraseña incorrectos"})

    else:
        form=AuthenticationForm()
        return render(request, "loginchat.html", {"formulario":form})

def registerchat(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "chathome.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registerchat.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})

    else:
        form=UserRegisterForm()
        return render(request, "registerchat.html", {"formulario":form})

@login_required
def chathome(request):
    if not request.user.is_authenticated:
        return render('index.html')
    if request.method == "GET":
        username = request.GET["username"]
        userlist = User.objects.filter(username=username)
        return render(request, "chathome.html", {'userlist':userlist})

def messagesbox(request, sender, receiver):
    if not request.user.is_authenticated:
        return render('index.html')
    if request.method == "GET":
        usuarios = User.objects.exclude(username=request.user.username)
        receptor = User.objects.get(id=receiver)
        mensajes = Messages.objects.filter(sender_id=sender, receiver_id=receiver)
        return render(request, "messagesbox.html", {'usuarios':usuarios, 'receptor':receptor, 'mensajes':mensajes})