from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import logoutView, RegisterView



urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logoutView, name='logout'),
]

