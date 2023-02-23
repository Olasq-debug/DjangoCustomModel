from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminUserConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'username', 'first_name')
    list_filter = ('is_staff', 'is_active', 'username', 'email')
    ordering = ["-start_date"]
    list_display = ('email', 'id', 'username', 
                    'first_name', 'is_staff', 'is_active' )

    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'email')}),
        ('Permission', {'fields': ('is_active', 'is_staff')}),
         ('Personal', {'fields': ('about',)}),
    )



admin.site.register(NewUser, AdminUserConfig)
