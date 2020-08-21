from django.db import models

class EmailSender(models.Model):
	email = models.EmailField(verbose_name="email", max_length=70, unique=True)

	def __str__(self):
		return self.email
