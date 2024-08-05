from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    login = models.CharField(max_length=55)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    social_links = models.TextField()

    def __str__(self):
        return self.login


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Public(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teg = models.TextField()
    category = models.ManyToManyField(Category, related_name='publics')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    public = models.ForeignKey(Public, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


