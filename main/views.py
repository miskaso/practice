from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm


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
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
