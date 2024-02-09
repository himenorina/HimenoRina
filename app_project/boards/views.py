from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, '掲示板を作成しました。')
        return redirect('accounts:home')
    return render(
        request, 'boards/create_theme.html', context={
            'create_theme_form':create_theme_form,
        }
    )