#from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'users/login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Привет {username.title()}, WELLCOME')
                return redirect('post-create')
            # form is not valid or user is not authenticated
        messages.error(request, 'invalid username or password')
        return render(request, 'users/login.html', {'form':form})
def sign_out(request):
    logout(request)
    messages.success(request, f'You are logout')
    return redirect('login')

# Create your views here.
