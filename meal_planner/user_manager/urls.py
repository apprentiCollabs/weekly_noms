from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import RegisterUser

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='path/to/template/goes/here.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='path/to/template/goes/here.html'), name='password_change'),
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(template_name='redirect/back/to/user/home.html'), name='password_change_done'),
    url(r'^$', RegisterUser.as_view(), name='register'),
]