from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.base.urls")),
    # path('about/', include("apps.about")),
    # path('blog/', include("apps.blog")),
    # path('contact/', include("apps.contact")),
    # path('package/', include("apps.package")),
    # path('service/', include("apps.service")),

] + debug_toolbar_urls()
# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)