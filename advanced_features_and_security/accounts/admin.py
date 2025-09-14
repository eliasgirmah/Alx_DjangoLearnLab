from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)