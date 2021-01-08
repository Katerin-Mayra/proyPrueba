#importando utiles
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

#importando modelos
from principal.models import Profile
from django.contrib.auth.models import User


#importando formularios
from principal.forms import FormPerfil
from django.contrib.auth.forms import UserCreationForm
from principal.forms import UserForm

#importando clases para CRUD
from django.views.generic import ListView



#vistas
#login
def user_login(request):
    if request.method == 'POST':
        #dos formas para sacar datos del request post
        username = request.POST.get('username')
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        #return HttpResponse(user.username + user.email )
        if user is not None:
            
            login(request, user)
            return redirect('inicio', id=user.username)

        else:
            return HttpResponse('Usuario no Valido')
        
    else:
        
        return render(request, 'login.html')
#logout
def log_out(request):
    logout(request)
    return redirect('login')

#inicio
def inicio_user(request, id):
    
    user = User.objects.get(username=id)

    if user.is_superuser:

        profiles = Profile.objects.all()
        users = User.objects.all()

        return render(request, 'admin_inicio.html', {
            'user': id,
            'profiles': profiles,
            'users': users,
            'nombre_usuario': id,
        })

    else:

        return render(request, 'user_inicio.html', {
            'user': "Usuario",
            'nombre_usuario': id,
        })
#lista de perfiles para admin
def list_profiles(request, id):
    profiles = Profile.objects.all()
    #return HttpResponse('perfiles')
    return render(request, 'admin_profiles.html', {
        'user': id,
        'profiles': profiles,
        'nombre_usuario': id,
    })

#registro de usuarios
def register_user(request, id):
    
    if request.method == 'POST':
        
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('inicio', id=id)
        else:
            return HttpResponse('error registro')

    else:
        form = UserForm()
        return render(request, 'registro_user.html', {
            'nombre_usuario': id,
            'form': form,
            'tittle': 'Usuario'
        })
#registro de perfiles
def register_profile(request, id):
    
    if request.method == 'POST':

        profile_form = FormPerfil(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('perfiles', id=id)
        else:
            return HttpResponse('error registro')

    else:
        form = FormPerfil()
        return render(request, 'registro_profile.html', {
            'nombre_usuario': id,
            'form': form,
            'tittle': 'Perfil',
        })
#vista para editar usuarios
def edit_user(request, id, id_user):
    user = User.objects.get(pk=id_user)
    if request.method == "GET":
        
        form = FormPerfil(instance=perfil)

    else:
        
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

        return redirect('inicio', id=id)
    
    return render(request, 'editar_user.html', {
        'nombre_usuario': id,
        'form': form,
        'id_user': id_user,
    })

#vista para editar perfiles
def edit_profile(request, id, id_profile):
    
    perfil = Profile.objects.get(pk=id_profile)
    if request.method == "GET":
        
        #return HttpResponse('get')
        form = FormPerfil(instance=perfil)
        #return HttpResponse('formulario con instancia')

    else:
        
        form = FormPerfil(request.POST, instance=perfil)

        if form.is_valid():
            form.save()

        return redirect('perfiles', id=id)
    
    #return HttpResponse('hasta aqui todo bien')
    return render(request, 'editar_profile.html', {
        'nombre_usuario': id,
        'form': form,
        'id_profile': id_profile,
    })

#vista para borrar usuarios
def delete_user(request, id, id_user):

    user = User.objects.get(pk=id_user)
    user.delete()
    return redirect('inicio', id=id)

#vista para borrar perfiles
def delete_profile(request, id, id_profile):
    
    perfil = Profile.objects.get(pk=id_profile)
    perfil.delete()
    
    return redirect('perfiles', id=id)

#subir perfil desde usuarios
def create_profile(request, id):
    
    user = User.objects.get(username=id)
    
    if request.method == 'POST':
        
        form = FormPerfil(request.POST)
        
        if form.is_valid():

            form.save()
            perfil = Profile.objects.get(email=user.email)
            perfil.user = user
            perfil.save()

        else:
            return HttpResponse('error de formulario')
        
        if user.is_superuser:
            return redirect('inicio', id=id)
        else:
            return redirect('user', id=user.username)

    else:

        try:
            perfil = Profile.objects.get(email = user.email)
            return render(request, 'profile.html', {
                'profile': perfil,
                'nombre_usuario': id,
            })
        except:
            formulario = FormPerfil()

            return render(request, 'user_profile.html', {
                    'form': formulario,
                    'nombre_usuario': id
            })

