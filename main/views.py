from django.shortcuts import render,redirect
from .models import Comment, Public
from django.contrib.auth.models import User
from .forms import CreatePublicForm
from django.views.generic import ListView

# Create your views here.


def index(req):
    return render(req, 'index.html')


class ViewPublic(ListView):
    model = Public
    template_name = 'view_public.html'
    context_object_name = 'view'


def create_public(req):
    if req.method == 'POST':
        form = CreatePublicForm()
        if form.is_valid():
            form.save()
            return redirect('allpublic')
    else:
        form = CreatePublicForm()
    return render(req, 'create_pubic.html', {'form': form})

