from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup_view, name='signup_view'),
    path('profile', views.profile_view, name='profile_view'),
    path('registration/logout', views.logout_view, name='logout_view'),
]