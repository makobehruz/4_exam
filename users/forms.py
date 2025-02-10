from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}))


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-3 py-2 border rounded-md'}),
                          required=False)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-md'}), required=False)
    phone_number = forms.CharField(max_length=15, required=False,
                                   widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        }

