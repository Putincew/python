from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required




def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skill = prof.skill_set.exclude(descriotions__exact='')
    other_skill = prof.skill_set.filter(descriotions='')

    context = {
        'profile': prof,
        'top_skill': top_skill,
        'other_skill': other_skill,
    }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Не корректное имя пользователя или пароль')

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Ann error has occured durring register')


    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
@login_required(login_url='login')
def user_account(request):
    prof = request.user.profile
    skills = prof.skill_set.all()
    projects = prof.project_set.all()
    context = {
        'profile': prof,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')



    context = {'form': form}
    return render(request, 'user/profile_form.html', context)

@login_required(login_url='login')
def create_skill(request):
    form = SkillForm()
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

