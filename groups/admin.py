from django.contrib import admin

from .models import Group
from students.admin import StudentInline


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'status', 'created_at')
    ordering = ['name']
    search_fields = ('name', 'desc')
    inlines = [StudentInline]