from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm,AuthenticattionForm,AccountUpdateForm
from accounts.models import Account
from blog.models import BlogPost

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')

def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('home')

	if request.POST:
		form = AuthenticattionForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email,password=password)

			if user:
				login(request, user)
				return redirect('home')
	else:
		form = AuthenticattionForm()

	context['login_form'] = form
	return render(request, 'account/sign_in.html', context)

def account_view(request):
	if not request.user.is_authenticated:
		return redirect("login")

	context={}
	context['is_online'] = Account.objects.values_list('is_online',flat=True).get(email = request.user.email)
	if request.POST:
		form = AccountUpdateForm(request.POST or None,request.FILES or None, instance = request.user)
		if form.is_valid():
			form.initial = {
				"email": request.user.email,
				"username": request.user.username,
				"image": request.user.image,
			}
			form.save()
			context['success_message'] = "Update"
	else:
		form = AccountUpdateForm(
				initial={
					"email": request.user.email,
					"username": request.user.username,
					"image": request.user.image,
				}
			)
	context['account_form'] = form

	blog_posts = BlogPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, "account/account_change.html", context)
	
def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html',{})

def must_be_a_admin(request):
	return render(request, 'account/must_be_a_admin.html',{})
