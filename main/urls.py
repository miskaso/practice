from django.urls import path, include
from .views import register, home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register),
]
