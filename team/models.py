from django.db import models

def upload_location(instance,filename):
	file_path = 'team/{name}/{filename}'.format(
									name=str(instance.name),
									filename = filename,
								
		)
	return file_path

class Team(models.Model):
	name = models.TextField(max_length=100, null=False, blank=True)
	about_person 	= models.TextField(max_length=1000, null=False, blank=True)
	picture		 	= models.ImageField(default='default_avatar.png', upload_to=upload_location, null=True, blank=True)
	facebook_link 	= models.TextField(max_length=1000, null=True, default='https://uk-ua.facebook.com/',	blank=True)
	instagram_link	= models.TextField(max_length=1000, null=True, default='https://www.instagram.com/',	blank=True)
	twitter_link 	= models.TextField(max_length=1000, null=True, default='https://twitter.com/explore/',	blank=True)
	github_link		= models.TextField(max_length=1000, null=True, default='https://github.com/',	blank=True)