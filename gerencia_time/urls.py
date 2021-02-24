from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastros/', include('apps.cadastros.urls')),
    path('', include('apps.core.urls')),
]

#personalização da template admin
admin.site.site_title = 'Gerenciador'
admin.site.site_header = 'Murici-FC'


