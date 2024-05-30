from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view

app_name = 'users'

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", authentication_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("profile/", views.profile, name='profile'),
    path("createprofile/", views.create_profile, name='createprofile'),
    path("sellerprofile/<int:id>/", views.seller_profile, name='sellerprofile'),
]
