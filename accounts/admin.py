from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Department,Branch


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
    ]

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('roll', 'active', 'salary','gender','department','branch','joined','mobile','thumb'),
        }),
    )
 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email','roll','salary','active','gender','department','branch','joined','mobile','thumb')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class DepartmentTable(admin.ModelAdmin):
    model = Department
    list_display = [
        "name",
        "history"
    ]

class BranchTable(admin.ModelAdmin):
    model = Branch
    list_display = [
        "name",
        "history"
    ]
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Branch, BranchTable)
admin.site.register(Department, DepartmentTable)
