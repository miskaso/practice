from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    social_links = models.TextField()
