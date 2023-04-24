from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mapa
from .forms import MapaForm, UserEditForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from web import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "El usuario ya existe, por favor pruebe con otro usuario")
            return redirect('inicio')
        
        if User.objects.filter(email=email):
            messages.error("El e-mail ya se encuentra registrado")
            return redirect('inicio')
        
        if len(username)>10:
            messages.error(request, "El usuario debe tener menos de 10 carácteres")

        if pass1 != pass2:
            messages.error(request, "Las contraseñas no coinciden")
    
        if not username.isalnum():
            messages.error(request, "El nombre de usuario debe contener carácteres alfanuméricos")
            return redirect('inicio')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        messages.success(request, "Tu cuenta fue creada con éxito.")

    return render(request,'paginas/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
       
        if User is not None: 
            login(request, user)
            return redirect('subir')
            
        else:
            messages.error(request, "Error en usuario y/o contraseña")
            return redirect ('sigin')


        
    return render(request, 'paginas/signin.html')




def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def mapas(request):
    mapas = Mapa.objects.all()
    return render(request, 'mapas/index.html', {'mapas': mapas})

def subir_pedido(request):
    formulario = MapaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mapas')
    return render(request, 'mapas/subir.html', {'formulario': formulario})
    

def editar(request, id):
    edicion = Mapa.objects.get(id=id)
    formulario = MapaForm(request.POST or None, instance=edicion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('mapas')
    return render(request, 'mapas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    mapeo = Mapa.objects.get(id=id)
    mapeo.delete()
    return redirect('mapas')
