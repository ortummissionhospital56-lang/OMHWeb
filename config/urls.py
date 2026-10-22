from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Hospital Administration"
admin.site.site_title = "Hospital Admin"
admin.site.index_title = "Manage website content"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hospital.urls")),
]

# Serves uploaded files during development. Use your web server in production.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
