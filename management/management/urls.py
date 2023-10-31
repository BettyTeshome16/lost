from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('founde.urls')),
    path('admin/login/', auth_views.LoginView.as_view(template_name='Logine.html'), name='login'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)