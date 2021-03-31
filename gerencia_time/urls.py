from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastros/', include('apps.cadastros.urls')),
    path('gerencia/', include('apps.gerencia.urls')),
    path('', include('apps.core.urls')),
    path('accounts', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#personalização da template admin
admin.site.site_title = 'Gerenciador'
admin.site.site_header = 'Murici-FC'


