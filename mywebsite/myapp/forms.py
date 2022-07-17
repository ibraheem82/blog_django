
from django import forms
from django.forms import ModelForm
from .models import Post


# ===> inheriting from model form
class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'writer']