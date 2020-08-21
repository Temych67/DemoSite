from django.shortcuts import render,redirect,get_object_or_404
from blog.models import BlogPost
from blog.forms import CreateBlogPostForm,UpdateBlogPostForm
from accounts.models import Account
from django.db.models import Q
from django.http import HttpResponse


def create_blog_view(request):
	context={}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	if not user.is_admin:
		return redirect('must_be_a_admin')
	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
		context['success_message'] = "Create"

	context['form']=form

	return render(request,'blog/create_blog.html',context)

def detail_blog_view(request, slug):

	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	if request.POST:
		blog_post.delete()
		return redirect('home')
	context['blog_post'] = blog_post
		
	return render(request, 'blog/detail_blog.html', context)

def edit_blog_view(request,slug):

	context={}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	if not user.is_admin:
		return redirect('must_be_a_admin')

	blog_post = get_object_or_404(BlogPost,slug=slug)

	if blog_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form=UpdateBlogPostForm(request.POST or None , request.FILES or None,instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj

	form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
		)

	context['form'] = form
	return render(request, 'blog/edit_blog.html', context)

def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	

def delete_blog_view(request,slug):
	context={}
	blog_post = get_object_or_404(BlogPost,slug=slug)

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	if blog_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if not user.is_admin:
		return redirect('must_be_a_admin')

	if request.POST:
		blog_post.delete()
		return redirect('home')
	context['blog_post'] = blog_post
	return render(request,'blog/delete_blog.html',context)
