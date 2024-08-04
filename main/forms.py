from django import forms
from .models import Public, Category, Comment


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
