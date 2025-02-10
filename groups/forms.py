from django import forms
from .models import Group, Subject


class GroupForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'space-y-2 text-white',
        }),
    )

    class Meta:
        model = Group
        fields = ['name', 'teacher', 'academic_year', 'grade', 'schedule', 'max_students', 'desc', 'subjects', 'status']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
                'placeholder': 'Enter group name',
            }),
            'grade': forms.Select( attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
            }),
            'teacher': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
            }),
            'schedule': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
            }),
            'academic_year': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
                'placeholder': 'e.g., 2023-2024',
            }),
            'max_students': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
                'placeholder': 'Enter maximum number of students',
            }),
            'desc': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white',
                'placeholder': 'Enter group description',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md bg-gray-900 text-white'
            }),
        }


