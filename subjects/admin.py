from django.contrib import admin

from .models import Subject


class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 1

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'grade', 'status', 'created_at')
    ordering = ['name']
    search_fields = ('name', 'desc')