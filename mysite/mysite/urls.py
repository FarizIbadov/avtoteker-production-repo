from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include,re_path

urlpatterns = [
    path("", include("main_site.urls")),
    path("",include("oilapp.urls")),
    # path("admin/", include("custom_admin.urls")),
    path("avtoadmin/", admin.site.urls),
    path("",include('wheel_size.urls')),
    path("campaigns/",include("campaign.urls")),
    path("blogs/",include("news.urls")),
    path("kredit/",include("kredit.urls")),
    # path("about-us/",include("about_us.urls")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
