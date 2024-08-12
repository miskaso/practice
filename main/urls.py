from django.urls import path, include
from .views import register, home_page
from . import views

urlpatterns = [
    path('', home_page, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('public/', views.ViewPublic.as_view(), name='allpublic'),
    path('public/create/', views.create_public, name='create'),
    path('public/<int:pk>/', views.DetailViewPublic.as_view(), name='detail'),
    path('public/<int:pk>/edit/', views.RedactorPublic.as_view(),
         name='public_edit'),
    path('delete/', views.delete_public, name='delete'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('search/', views.get_search, name='search'),
    path('category/', views.categories, name='category'),
    path('get_category/<str:name>', views.get_category, name='get_category'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.get_profile, name='profile'),



]