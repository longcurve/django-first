# Views for mysite->blog

from django.shortcuts import render, redirect
from django.template import loader
from blog.models import Post
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    elif request.method == "GET":
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')