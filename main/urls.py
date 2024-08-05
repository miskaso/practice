from django.urls import path, include
from .views import register, home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register),
    path('', views.index, name='home'),
    path('publics/', views.ViewPublic.as_view(), name='allpublic'),
    path('create/', views.create_public, name='create'),

]