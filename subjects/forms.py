from django import forms

from .models import Subject, Prerequisite


class SubjectForm(forms.ModelForm):
    prerequisites = forms.ModelMultipleChoiceField(
        queryset=Prerequisite.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        }),
    )

    class Meta:
        model = Subject
        fields = ['name', 'department', 'desc', 'credit_hours', 'grade', 'prerequisites', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject name',
            }),
            'department': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',

            }),
            'desc': forms.Textarea( attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject description'
            }),
            'credit_hours': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter credit hours',
            }),
            'grade': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }

