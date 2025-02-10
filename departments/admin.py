from django.contrib import admin

from .models import Department
from subjects.admin import SubjectInline


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'created_at')
    ordering = ['name']
    search_fields = ('name', 'desc')
    inlines = [SubjectInline]