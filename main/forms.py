from django import forms
from .models import Public, Category, Comment, Profile
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    company = forms.CharField(max_length=255)
    job_title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    social_links = forms.TextInput()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'company', 'job_title', 'description', 'social_links']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        profile = Profile(user=user, company=self.cleaned_data['company'],
                          job_title=self.cleaned_data['job_title'],
                          description=self.cleaned_data['description'],
                          social_links=self.cleaned_data['social_links'])
        if commit:
            profile.save()
        return profile

      
class CreatePublicForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, label='Категории')

    class Meta:
        model = Public
        fields = ['title', 'text', 'teg', 'category']

        labels = {
            'title': 'Название',
            'text': 'Текст',
            'teg': 'Теги',

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите название статьи'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваша мысль )'}),
            'teg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите теги через запятую'}),

        }

        error_messages = {
            'title': {
                'required': 'Пожалуйста, введите название статьи',
                'max_length': 'Название статьи не должно превышать 10 символов'
            },
            'text': {
                'required': 'Это поле не может быть пустым'
            }


        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']




# class RedactorPublicForm(forms.ModelForm):
#     title = forms.CharField(max_length=55)
#     text = forms.TextInput()
#     teg = forms.TextInput()
#
#     class Meta:
#         model = Public
#         fields = ['title', 'text', 'teg']
#
#     def save(self, commit=True):
#         public = Public.objects.create_public(
#             title=self.cleaned_data['title'],
#             text=self.cleaned_data['text'],
#             teg=self.cleaned_data['tag']
#         )
#         result = Public(public)
#         if commit:
#             result.save()
#         return result

