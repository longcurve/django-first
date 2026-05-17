from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup_view, name='signup_view'),
    path('logout', views.logout, name='logout')
]