from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reader/', include('Reader.urls')),  
    path('login/', include('Login.urls')),
    path('writer/', include('Writer.urls')),
    path('dashboard/', include('Dashboard.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
