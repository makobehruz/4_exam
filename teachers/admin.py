from django.contrib import admin

from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'status', 'created_at')
    ordering = ['id']
    search_fields = ('first_name', 'last_name', 'address')