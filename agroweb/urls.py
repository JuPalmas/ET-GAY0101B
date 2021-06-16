from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login,logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
]