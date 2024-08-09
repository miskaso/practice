
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Public, Category
from django.contrib.auth.models import User
from .forms import CreatePublicForm, CommentForm, RegisterForm
from django.views.generic import ListView, DetailView, UpdateView


# Create your views here.

@login_required
def home_page(request):
    home_page_1 = ['Приветствуем на главной странице!']
    return render(request, 'index.html', {'home_page_1': home_page_1})

def product_list(request):
    selected_category = request.GET.get('category')
    products = Product.objects.all()
    if selected_category:
        products = products.filter(category=selected_category)
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    })


def search(request):
    category = request.GET.get('category')
    products = Public.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'category.html', {'products': products,
            'categories': categories,
            'select': category})


class ViewPublic(ListView):
    model = Public
    template_name = 'view_public.html'
    context_object_name = 'view'


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class DetailViewPublic(DetailView):
    model = Public
    template_name = 'detail_public.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.all().order_by('-datetime')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        form = CommentForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.public = self.object
            message.save()
            return redirect('detail', pk=self.object.pk)

        context['form'] = form
        return self.render_to_response(context)


def delete_comment(req):
    if req.method == 'POST':
        mes_id = req.POST.get('id')
        chat = get_object_or_404(Comment, id=mes_id)
        public = chat.public.id
        chat.delete()
        return redirect('detail', pk=public)


def create_public(req):
    if req.method == 'POST':
        form = CreatePublicForm(req.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = req.user
            result.save()
            return redirect('allpublic')
    else:
        form = CreatePublicForm()
    return render(req, 'create_pubic.html', {'form': form})


class RedactorPublic(UpdateView):
    model = Public
    fields = ['title', 'text', 'teg']
    template_name = 'update.html'
    success_url = '../'

    def get_object(self, queryset=None):
        public = get_object_or_404(Public, id=self.kwargs['pk'],
                                   user=self.request.user)
        return public


def delete_public(req):
    if req.method == 'POST':
        pub_id = req.POST.get('id')
        public = get_object_or_404(Public, id=pub_id)
        public.delete()
        return redirect('../public/')

