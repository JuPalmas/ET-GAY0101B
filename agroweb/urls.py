from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login,logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
