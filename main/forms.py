from django import forms
from .models import Public


class CreatePublicForm(forms.ModelForm):
    class Meta:
        model = Public
        fields = '__all__'

