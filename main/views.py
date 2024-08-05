from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.shortcuts import render,redirect
from .models import Comment, Public
from django.contrib.auth.models import User
from .forms import CreatePublicForm
from django.views.generic import ListView

# Create your views here.

@login_required
def home_page(request):
    home_page_1 = ['Приветствуем на главную страницу!']
    response = render(request, 'home_page.html', {'home_page_1': home_page_1})
    return response


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
def create_public(req):
    if req.method == 'POST':
        form = CreatePublicForm()
        if form.is_valid():
            form.save()
            return redirect('allpublic')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

        form = CreatePublicForm()
    return render(req, 'create_pubic.html', {'form': form})

