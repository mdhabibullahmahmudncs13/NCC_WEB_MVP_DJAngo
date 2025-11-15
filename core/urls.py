from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Public pages
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    
    # Segments
    path('segments/', views.SegmentListView.as_view(), name='segments'),
    path('segments/<int:pk>/', views.SegmentDetailView.as_view(), name='segment_detail'),
    
    # Members
    path('members/', views.MemberListView.as_view(), name='members'),
    
    # Achievements
    path('achievements/', views.AchievementListView.as_view(), name='achievements'),
    
    # Gallery
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    
    # Events
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    
    # Blog/News
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    
    # Projects
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    # Resources
    path('resources/', views.ResourceListView.as_view(), name='resources'),
    path('resources/<int:pk>/download/', views.resource_download, name='resource_download'),
    
    # FAQ
    path('faq/', views.faq_view, name='faq'),
    
    # Contact & Communication
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    
    # Membership
    path('join/', views.MembershipApplicationView.as_view(), name='membership_application'),
    path('join/success/', views.membership_success_view, name='membership_success'),
    
    # Search
    path('search/', views.search_view, name='search'),
    
    # SEO
    path('robots.txt', views.robots_txt, name='robots_txt'),
    
    # Admin dashboard
    path('admin/dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]