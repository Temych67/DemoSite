from django import forms
from send_email.models import EmailSender


class EmailSenderForm(forms.ModelForm):
	class Meta:
		model = EmailSender
		fields = "__all__"