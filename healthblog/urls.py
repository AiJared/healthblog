from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from healthb.sitemaps import PostSitemap
from healthb.feeds import LatestPostsFeed

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('healthb.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("feed/rss/", LatestPostsFeed(), name="post_feed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)