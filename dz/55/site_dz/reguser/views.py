from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'reguser/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'reguser/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'
            })
        else:
            login(request, user)
            return redirect('index')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'reguser/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'reguser/signupuser.html', {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует'})
        else:
            return render(request, 'reguser/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

