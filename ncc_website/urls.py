"""
URL configuration for ncc_website project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import (
    StaticViewSitemap, SegmentSitemap, EventSitemap, 
    BlogPostSitemap, ProjectSitemap, AchievementSitemap
)

sitemaps = {
    'static': StaticViewSitemap,
    'segments': SegmentSitemap,
    'events': EventSitemap,
    'blog': BlogPostSitemap,
    'projects': ProjectSitemap,
    'achievements': AchievementSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('core.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
