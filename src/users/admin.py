from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser,Notification
from users.forms import CustomUserForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'nome', 'cognome']  
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('nome', 'cognome', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined'), 'classes': ('collapse',)}),  # Imposta il campo last_login come readonly
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login','date_joined') 

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Notification)
