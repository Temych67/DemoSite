from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



from index.views import(
		home_screen_view,
		info_screen_view,
		info_screen_two_view,
	)

from accounts.views import(
	registration_view,
	logout_view,
	login_view,
    must_authenticate_view,
    account_view,
    must_be_a_admin,
	)

urlpatterns = [

	path('admin/', admin.site.urls),

	path('account/',account_view,name='account'),  
	path('login/',login_view,name='login'),
	path('register/',registration_view,name='register'),
	path('logout/',logout_view,name='logout'),
	path('must_authenticate/',must_authenticate_view,name='must_authenticate'),
	path('must_be_a_admin/',must_be_a_admin,name='must_be_a_admin'),

	path('blog/',include('blog.urls','blog')),
	
	path('accounts/', include('allauth.urls')),

	path('',home_screen_view,name='home'),
	path('info/',info_screen_view,name='info'),
	path('info2/',info_screen_two_view,name='info2'),

	# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
		name='password_change_done'),

	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
		name='password_change'),

	path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
		name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
		name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  