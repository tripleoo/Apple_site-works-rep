from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iphone.urls')),
    path('users/', include('users.urls', namespace='users')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Управление сайтом"
admin.site.index_title = "Apple technics"