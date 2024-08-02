from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('publics/', views.ViewPublic.as_view(), name='allpublic'),
    path('create/', views.create_public, name='create'),

]