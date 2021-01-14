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
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



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
            return redirect('inicio')

        else:
            return HttpResponse('Usuario no Valido')
        
    else:
        
        return render(request, 'login.html')
#logout
def log_out(request):
    logout(request)
    return redirect('login')

#inicio
def inicio_user(request):
    if request.user.is_superuser:
        return render(request, 'user_inicio.html')  
    return render(request, 'user_inicio2.html')  

#lista de usuarios para admin
def list_users(request):
    #return HttpResponse('lista de usuarios')
    users = User.objects.all()

    return render(request, 'admin_users.html', {
        'users': users,
    })

#lista de perfiles para admin
def list_profiles(request):
    
    profiles = Profile.objects.all()

    return render(request, 'admin_profiles.html', {
        'profiles': profiles,
    })

#registro de usuarios
def register_user(request):
    
    if request.method == 'POST':
        
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('inicio')
        else:
            return HttpResponse('error registro')

    else:
        form = UserForm()
        return render(request, 'registro_user.html', {
            'form': form,
            'tittle': 'Usuario'
        })
#registro de perfiles
def register_profile(request):
    
    if request.method == 'POST':

        profile_form = FormPerfil(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('perfiles')
        else:
            return HttpResponse('error registro')

    else:
        form = FormPerfil()
        return render(request, 'registro_profile.html', {
            'form': form,
            'tittle': 'Perfil',
        })
#vista para editar usuarios
def edit_user(request, id_user):
    user = User.objects.get(pk=id_user)
    if request.method == "GET":
        
        form = FormPerfil(instance=perfil)

    else:
        
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

        return redirect('inicio')
    
    return render(request, 'editar_user.html', {
        'form': form,
        'id_user': id_user,
    })

#vista para editar perfiles
def edit_profile(request, id_profile):
    
    perfil = Profile.objects.get(pk=id_profile)
    if request.method == "GET":
        
        #return HttpResponse('get')
        form = FormPerfil(instance=perfil)
        #return HttpResponse('formulario con instancia')

    else:
        
        form = FormPerfil(request.POST, instance=perfil)

        if form.is_valid():
            form.save()

        return redirect('perfiles')
    
    #return HttpResponse('hasta aqui todo bien')
    return render(request, 'editar_profile.html', {
        'form': form,
        'id_profile': id_profile,
    })

#vista para borrar usuarios
def delete_user(request, id_user):

    user = User.objects.get(pk=id_user)
    user.delete()
    return redirect('inicio')

#vista para borrar perfiles
def delete_profile(request, id_profile):
    
    perfil = Profile.objects.get(pk=id_profile)
    perfil.delete()
    
    return redirect('perfiles')

#subir perfil desde usuarios
def create_profile(request, id_user):
    
    user = User.objects.get(username=id_user)
    #return HttpResponse(user.email)

    if request.method == 'POST':
        
        form = FormPerfil(request.POST)
        
        if form.is_valid():

            form.save()
            perfil = Profile.objects.get(email=user.email)
            perfil.user = user
            perfil.save()

        else:
            return HttpResponse('error de formulario')
        
        return redirect('inicio')

    else:
        try:
            perfil = Profile.objects.get(email = user.email)
            
            return render(request, 'profile.html', {
                'profile': perfil,
            })
        except:
            
            formulario = FormPerfil()
            
            return render(request, 'user_profile.html', {
                    'form': formulario,
            })

#listar usuarios con clase
class UserList(ListView):
    model = User
    template_name = 'admin_users.html'

#listar perfiles conm clase :v
class ProfileList(ListView):
    model = Profile
    template_name = 'admin_profiles.html'

#registrar usuarios con clase
class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro_user.html'
    success_url = reverse_lazy('usuarios')

#registrar perfiles con clase :v
class ProfileCreate(CreateView):
    model = Profile
    form_class = FormPerfil
    template_name = 'registro_profile.html'
    success_url = reverse_lazy('perfiles')

#actualizar usuarios
class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'editar_user.html'
    success_url = reverse_lazy('usuarios')

#actualizar perfiles
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = FormPerfil
    template_name = 'editar_profile.html'
    success_url = reverse_lazy('perfiles')

#borrar usuarios
class UserDelete(DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('usuarios')

#borrar perfiles
class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('perfiles')