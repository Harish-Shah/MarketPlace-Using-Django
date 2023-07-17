from django.contrib.auth import views as auth_views
from django.urls import path
from .import views as v
from .forms import LoginForm

app_name='core'

urlpatterns=[
    path('',v.index,name='index'),
    path('contact/',v.contact,name='contact'),
    path('signup/',v.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
]