
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('Book.api.urls')),
    path('users/', include('Users.api.urls')),
    
]
