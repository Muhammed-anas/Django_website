from django.urls import path
from django import urls
from .views import home_view, Register_view, Login_view, logout_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('register/', Register_view.as_view(), name='register'),
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
