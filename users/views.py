from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UpdateProfileForm
from django.contrib.auth.forms import PasswordChangeForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your profile was successfully updated!')

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')

            return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'users/profile-update.html', {'form': form, 'password_form': password_form})


@login_required
def dashboard(request):
    # Your existing dashboard logic here
    return render(request, 'dashboard.html')

