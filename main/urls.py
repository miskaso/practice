from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('public/', views.ViewPublic.as_view(), name='allpublic'),
    path('public/create/', views.create_public, name='create'),
    path('public/<int:pk>/', views.DetailViewPublic.as_view(), name='detail'),
    path('public/<int:pk>/edit/', views.RedactorPublic.as_view(),
         name='public_edit'),
    path('delete/', views.delete_public, name='delete'),
    path('delete_comment/', views.delete_comment, name='delete_comment')
]