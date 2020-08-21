# Generated by Django 3.0.1 on 2020-07-06 18:18

from django.db import migrations, models
import team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100)),
                ('about_person', models.TextField(blank=True, max_length=1000)),
                ('picture', models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to=team.models.upload_location)),
                ('facebook_link', models.TextField(blank=True, default='https://uk-ua.facebook.com/', max_length=1000, null=True)),
                ('instagram_link', models.TextField(blank=True, default='https://www.instagram.com/', max_length=1000, null=True)),
                ('twitter_link', models.TextField(blank=True, default='https://twitter.com/explore/', max_length=1000, null=True)),
                ('github_link', models.TextField(blank=True, default='https://github.com/', max_length=1000, null=True)),
            ],
        ),
    ]