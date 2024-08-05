from django.contrib import admin
from .models import Profile, Category, Comment, Public

# Register your models here.

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Public)
