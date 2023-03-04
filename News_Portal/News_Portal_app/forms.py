from django_filters import DateFilter
from django import forms
from .models import Post, Author, Category
from django.core.exceptions import ValidationError
from datetime import datetime
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class PostForm(forms.ModelForm):
    heading = forms.CharField(min_length=20)
    author = Author.objects.all().values('auth__username')         #.values('auth')
    categories = Category.objects.all().values('cat_name')

    class Meta:
        model = Post
        fields = [
            'heading',
            'author',
            'text',
            'categories'
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        text = cleaned_data.get("text")
        if heading == text:
            raise ValidationError("Описание не должно быть идентично названию.")
        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
