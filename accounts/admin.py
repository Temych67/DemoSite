from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):
	list_display = ('username','email','date_joined','last_login','is_admin','is_staff')
	search_fields = ('username','email')
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.site_header = 'Django Admin Panel'
admin.site.register(Account, AccountAdmin)