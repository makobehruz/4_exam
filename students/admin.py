from django.contrib import admin

from .models import Student

class StudentInline(admin.StackedInline):
    model = Student
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'status', 'created_at')
    ordering = ['first_name']
    search_fields = ('first_name', 'last_name', 'address')