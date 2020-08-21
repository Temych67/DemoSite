from django.contrib import admin
from send_email.models import EmailSender


class EmailSenderAdmin(admin.ModelAdmin):
	list_display = ('email')
		
admin.site.register(EmailSender)