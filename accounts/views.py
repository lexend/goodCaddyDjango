from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm, LoginForm
#from django.contrib.auth.forms import UserCreationForm

#from .models import accounts

#def index(request):
#    return render(request, 'accounts/index.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:member'))
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('accounts:member'))
    return render(request, 'accounts/register.html', {'register_form': register_form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:member'))
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('accounts:member'))
    return render(request, 'accounts/login.html', {'login_form': login_form})

#def register_view(request):
#    form = SignUpForm(request.POST)
#    if form.is_valid():
#        user = form.save()
#        user.refresh_from_db()
#        user.profile.first_name = form.cleaned_data.get('first_name')
#        user.profile.last_name = form.cleaned_data.get('last_name')
#        user.profile.email = form.cleaned_data.get('email')
#        user.save()
#        username = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password1')
#        user = authenticate(username=username, password=password)
#        login(request, user)
#        return redirect('accounts/login')
#    else:
#        form = SignUpForm()
#    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('start:index'))

@login_required
def member_view(request):
    return render(request, 'accounts/member.html')
