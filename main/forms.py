from django import forms
from .models import Public, Category, Comment



class RegisterForm(forms.ModelForm):
    user = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    company = forms.CharField(max_length=255)
    job_title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    social_links = forms.CharField(max_length=255)

    class Meta:
        model = Profile
        fields = ['user', 'email', 'password', 'company', 'job_title', 'description', 'social_links']

    def save(self, commit=True):
        user = User.objects.create_user(
            user=self.cleaned_data['user'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'])
        profile = Profile(user=user, company=self.cleaned_data['company'],
                          job_title=self.cleaned_data['job_title'],
                          description=self.cleaned_data['description'],
                          social_links=self.cleaned_data['social_links'])
        if commit:
            profile.save()
        return profile

      
class CreatePublicForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select)

    class Meta:
        model = Public
        fields = ['title', 'text', 'teg', 'category']


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

