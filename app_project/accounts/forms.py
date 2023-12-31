from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')    
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())    
    
    class Meta():
        model = Users
        fields = ('username', 'email', 'password')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    picture = forms.FileField(label='写真', required=False)

    class Meta:
        model = Users
        fields = ('username', 'email', 'picture')


class PasswordChangeForm(forms.ModelForm):

    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    
    class Meta():
        model = Users
        fields = ('password', )
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user