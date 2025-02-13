from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}), label="Password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("This email is not registered.")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")

        return cleaned_data

class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-3 py-2 border rounded-md'}), required=False)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-md'}), required=False)
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['username'].initial = self.instance.username

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
        }
