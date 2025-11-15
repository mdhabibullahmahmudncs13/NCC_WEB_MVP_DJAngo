from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Segment, Event, BlogPost, Project, Achievement


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'core:home', 'core:about', 'core:segments', 'core:members',
            'core:achievements', 'core:gallery', 'core:events', 'core:blog',
            'core:projects', 'core:resources', 'core:faq', 'core:contact',
            'core:membership_application'
        ]

    def location(self, item):
        return reverse(item)


class SegmentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Segment.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class EventSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class BlogPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class AchievementSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Achievement.objects.all()

    def lastmod(self, obj):
        return obj.updated_at