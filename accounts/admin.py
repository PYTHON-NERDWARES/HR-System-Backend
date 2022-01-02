from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser, Branch, Department
from .forms import CustomUserCreationForm, CustomUserChangeForm



class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_staff','is_superuser')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')
    list_filter = ()


    fieldsets = UserAdmin.fieldsets + (
        ("Employee Info", {"fields": ('role', 'work_type', 'department', 'branch', 'experience', 'salary',
         'nationality','marital_status','gender', 'phone', 'Personal_Picture', 'annual_off_days', 'days_taken', 'days_remaining'), }),
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

admin.site.register(CustomUser, AccountAdmin)
admin.site.register(Department ,DepartmentTable)
admin.site.register(Branch, BranchTable)