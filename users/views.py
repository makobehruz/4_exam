from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UpdateProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                login(request, user)
                return redirect('home')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')

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

        if form.is_valid() and password_form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exclude(pk=request.user.pk).exists():
                messages.error(request, 'This username is already taken.')
            else:
                user = form.save()
                messages.success(request, 'Your profile was successfully updated!')

                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')

            return redirect('home')

        elif not password_form.is_valid():
            messages.error(request, 'Please correct the errors in the password form.')

    else:
        form = UpdateProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'users/profile-update.html', {'form': form, 'password_form': password_form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
