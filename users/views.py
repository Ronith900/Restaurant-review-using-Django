from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant.models import restaurant
from .models import user
from .forms import UserRegisterForm,commentform




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def review(request):
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.rest = restID
            comment.user = request.user
            comment.save
            return redirect('login')
    else:
        form = commentform()
        return render(request, 'users/user_form.html', {'form': form})