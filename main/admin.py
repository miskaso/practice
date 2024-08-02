from django.contrib import admin
from .models import Comment, Public, Category
# Register your models here.

admin.site.register(Public)
admin.site.register(Comment)
admin.site.register(Category)
