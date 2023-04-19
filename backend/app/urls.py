from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include,re_path
from django.conf.urls.i18n import i18n_patterns

import private_storage.urls

urlpatterns = i18n_patterns(
    path("", include("main_site.urls")),
    path("", include("tireapp.urls")),
    path("",include("oilapp.urls")),
    path("",include('wheel_size.urls')),
    path("campaigns/",include("campaign.urls")),
    path("blogs/",include("news.urls")),  
    path("about-us/", include('about.urls')),
    path('',include('ordering.urls')),
    path("", include("kapital_bank.urls")),
)


urlpatterns += [ 
    path("admin/", admin.site.urls),
    path("admin-translation/", include('rosetta.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^private-media/', include(private_storage.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
