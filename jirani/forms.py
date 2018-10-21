from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post,Business,Comments


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date', 'profile', 'location','comment']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['pub_date','neighborhood']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [ 'comment' ]

