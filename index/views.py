from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from send_email.forms import EmailSenderForm

from team.models import Team
from blog.views import get_blog_queryset
from operator import attrgetter


def home_screen_view(request):
	context={}
	email_form =  EmailSenderForm(request.POST)
	
	template = render_to_string("baseFolder/email_template.html", {'name': request.user.username})
	

	if request.POST:
		if email_form.is_valid():

			
			email_form.save()

			send_mail(
				'Thanks for you subscription',
				template,
				settings.EMAIL_HOST_USER,
				[request.POST.get('email'),],
				fail_silently=False,
				)

	return render(request, "baseFolder/base.html", context)

def info_screen_view(request):
	context={}
	query = ""
	query = request.GET.get('q', '')
	context['query'] = str(query)
	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	context['blog_posts'] = blog_posts
	context['teams'] = Team.objects.all()
	return render(request, "baseFolder/info.html", context)

def info_screen_two_view(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	context={}
	return render(request, "baseFolder/info2.html", context)