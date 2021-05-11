from django.contrib import admin
from accounts.models import Accounts
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountsAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_staff', 'is_admin', 'is_active')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',)

    # TODO: Add side filter
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Accounts, AccountsAdmin)
