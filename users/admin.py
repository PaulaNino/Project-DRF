from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_admin')