from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import RegisterUser, Index

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='/registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='path/to/template/goes/here.html'), name='password_change'),
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(template_name='redirect/back/to/user/home.html'), name='password_change_done'),
    url(r'^register/$', RegisterUser.as_view(), name='register'),
    url(r'^$', Index.as_view(), name='index')
]

# NOTE for Patrick: any reason why you didn't use core_views.signup instead of register? I'm look at https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html and using that as a guide for new user registration. Let me know your thoughts.
