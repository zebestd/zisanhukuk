from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    username = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "Kullanici"}))
    email = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "E-Posta"}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "Isim"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "Soyisim"}))
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput({ "placeholder": "Sifre"}))
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput({ "placeholder": "Sifre Tekrar"}))

#Girisim
class HaberForm(ModelForm):
    class Meta:
         model = Haber
         fields = ('isim', 'aciklama', 'dosya', 'resim')

class YorumForm(ModelForm):
    class Meta:
         model = Yorum
         fields = ('isim', 'aciklama', 'dosya', 'resim')

#Sorya
class SoruForm(ModelForm):
    class Meta:
         model = Post
         fields = ('isim', 'soru', 'aciklama')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['isim', 'yanit']


