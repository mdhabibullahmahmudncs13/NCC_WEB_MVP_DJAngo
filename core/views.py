from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import Q, Count
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Segment, Member, Achievement, GalleryPhoto, Event,
    ContactSubmission, Newsletter, BlogPost, FAQ, Project, 
    Resource, MembershipApplication
)
from .forms import (
    ContactForm, NewsletterForm, MembershipApplicationForm,
    SearchForm
)


def home_view(request):
    """Homepage view with segments showcase"""
    segments = Segment.objects.all()[:6]  # Show first 6 segments
    recent_news = BlogPost.objects.filter(status='published')[:3]
    upcoming_events = Event.objects.filter(status='upcoming')[:3]
    featured_projects = Project.objects.filter(status='completed')[:3]
    
    context = {
        'segments': segments,
        'recent_news': recent_news,
        'upcoming_events': upcoming_events,
        'featured_projects': featured_projects,
        'page_title': 'NITER Computer Club'
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    """About page view"""
    context = {
        'page_title': 'About - NITER Computer Club'
    }
    return render(request, 'core/about.html', context)


class SegmentListView(ListView):
    """List all segments"""
    model = Segment
    template_name = 'core/segments.html'
    context_object_name = 'segments'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Segments - NITER Computer Club'
        return context


class SegmentDetailView(DetailView):
    """Segment detail page with members"""
    model = Segment
    template_name = 'core/segment_detail.html'
    context_object_name = 'segment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        segment = self.get_object()
        context['members'] = segment.members.all()
        context['page_title'] = f'{segment.title} - NITER Computer Club'
        return context


class MemberListView(ListView):
    """List all members"""
    model = Member
    template_name = 'core/members.html'
    context_object_name = 'members'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Panel - NITER Computer Club'
        context['segments'] = Segment.objects.all()
        return context

    def get_queryset(self):
        queryset = Member.objects.all()
        segment_filter = self.request.GET.get('segment')
        if segment_filter:
            queryset = queryset.filter(segment__id=segment_filter)
        return queryset


class AchievementListView(ListView):
    """List all achievements"""
    model = Achievement
    template_name = 'core/achievements.html'
    context_object_name = 'achievements'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Achievements - NITER Computer Club'
        context['categories'] = Achievement.CATEGORY_CHOICES
        return context

    def get_queryset(self):
        queryset = Achievement.objects.all()
        category_filter = self.request.GET.get('category')
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset


class GalleryListView(ListView):
    """Gallery view"""
    model = GalleryPhoto
    template_name = 'core/gallery.html'
    context_object_name = 'photos'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Gallery - NITER Computer Club'
        context['categories'] = GalleryPhoto.CATEGORY_CHOICES
        return context

    def get_queryset(self):
        queryset = GalleryPhoto.objects.all()
        category_filter = self.request.GET.get('category')
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset


class EventListView(ListView):
    """List all events"""
    model = Event
    template_name = 'core/events.html'
    context_object_name = 'events'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Events - NITER Computer Club'
        context['statuses'] = Event.STATUS_CHOICES
        return context

    def get_queryset(self):
        queryset = Event.objects.all()
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset


class EventDetailView(DetailView):
    """Event detail page"""
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['page_title'] = f'{event.title} - NITER Computer Club'
        return context


# Admin Dashboard Views
@staff_member_required
def admin_dashboard_view(request):
    """Admin dashboard with statistics"""
    context = {
        'segments_count': Segment.objects.count(),
        'members_count': Member.objects.count(),
        'achievements_count': Achievement.objects.count(),
        'photos_count': GalleryPhoto.objects.count(),
        'events_count': Event.objects.count(),
        'projects_count': Project.objects.count(),
        'blog_posts_count': BlogPost.objects.count(),
        'applications_count': MembershipApplication.objects.filter(status='pending').count(),
        'contact_submissions': ContactSubmission.objects.filter(is_read=False).count(),
        'newsletter_subscribers': Newsletter.objects.filter(is_active=True).count(),
        'recent_members': Member.objects.order_by('-created_at')[:5],
        'recent_achievements': Achievement.objects.order_by('-created_at')[:5],
        'upcoming_events': Event.objects.filter(status='upcoming').order_by('date')[:5],
        'recent_applications': MembershipApplication.objects.order_by('-submitted_at')[:5],
        'page_title': 'Dashboard - NCC Admin'
    }
    return render(request, 'admin/dashboard.html', context)


# Contact and Communication Views
def contact_view(request):
    """Contact form and information"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact Us - NITER Computer Club'
    }
    return render(request, 'core/contact.html', context)


def newsletter_subscribe(request):
    """Newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Successfully subscribed!'})
                messages.success(request, 'Successfully subscribed to our newsletter!')
            except:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'message': 'Email already subscribed.'})
                messages.warning(request, 'This email is already subscribed.')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Please enter a valid email.'})
            messages.error(request, 'Please enter a valid email address.')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


# Blog Views
class BlogListView(ListView):
    """List published blog posts"""
    model = BlogPost
    template_name = 'core/blog.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return BlogPost.objects.filter(status='published').order_by('-published_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'News & Updates - NITER Computer Club'
        return context


class BlogDetailView(DetailView):
    """Blog post detail view"""
    model = BlogPost
    template_name = 'core/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return BlogPost.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['page_title'] = f'{post.title} - NITER Computer Club'
        context['related_posts'] = BlogPost.objects.filter(
            status='published'
        ).exclude(id=post.id).order_by('-published_at')[:3]
        return context


# FAQ View
def faq_view(request):
    """FAQ page"""
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'question')
    categories = FAQ.objects.filter(is_active=True).values_list('category', flat=True).distinct()
    
    context = {
        'faqs': faqs,
        'categories': categories,
        'page_title': 'FAQ - NITER Computer Club'
    }
    return render(request, 'core/faq.html', context)


# Projects Views
class ProjectListView(ListView):
    """List all projects"""
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Projects - NITER Computer Club'
        context['statuses'] = Project.STATUS_CHOICES
        context['segments'] = Segment.objects.all()
        return context
    
    def get_queryset(self):
        queryset = Project.objects.all()
        status_filter = self.request.GET.get('status')
        segment_filter = self.request.GET.get('segment')
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if segment_filter:
            queryset = queryset.filter(segment__id=segment_filter)
            
        return queryset


class ProjectDetailView(DetailView):
    """Project detail view"""
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['page_title'] = f'{project.title} - NITER Computer Club'
        context['related_projects'] = Project.objects.filter(
            segment=project.segment
        ).exclude(id=project.id)[:3]
        return context


# Resources Views
class ResourceListView(ListView):
    """List all resources"""
    model = Resource
    template_name = 'core/resources.html'
    context_object_name = 'resources'
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Resources - NITER Computer Club'
        context['categories'] = Resource.CATEGORY_CHOICES
        context['featured_resources'] = Resource.objects.filter(is_featured=True)[:5]
        return context
    
    def get_queryset(self):
        queryset = Resource.objects.all()
        category_filter = self.request.GET.get('category')
        search_query = self.request.GET.get('search')
        
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(tags__icontains=search_query)
            )
            
        return queryset


def resource_download(request, pk):
    """Handle resource downloads"""
    resource = get_object_or_404(Resource, pk=pk)
    
    if resource.file:
        # Increment download count
        Resource.objects.filter(pk=pk).update(downloads=resource.downloads + 1)
        
        response = HttpResponse(resource.file.read())
        response['Content-Disposition'] = f'attachment; filename="{resource.file.name}"'
        return response
    elif resource.external_url:
        # Increment download count for external links too
        Resource.objects.filter(pk=pk).update(downloads=resource.downloads + 1)
        return redirect(resource.external_url)
    else:
        raise Http404("Resource file not found")


# Membership Application Views
class MembershipApplicationView(CreateView):
    """Membership application form"""
    model = MembershipApplication
    form_class = MembershipApplicationForm
    template_name = 'core/membership_application.html'
    success_url = reverse_lazy('core:membership_success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Join Us - NITER Computer Club'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Your application has been submitted successfully! We will review it and get back to you.')
        return super().form_valid(form)


def membership_success_view(request):
    """Membership application success page"""
    context = {
        'page_title': 'Application Submitted - NITER Computer Club'
    }
    return render(request, 'core/membership_success.html', context)


# SEO and Utility Views
def robots_txt(request):
    """Generate robots.txt for SEO"""
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /media/",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


# Search functionality
def search_view(request):
    """Global search across all content"""
    form = SearchForm(request.GET or None)
    results = {}
    query = ''
    category = 'all'
    
    if form.is_valid():
        query = form.cleaned_data['query']
        category = form.cleaned_data['category'] or 'all'
        
        if category == 'all' or category == 'members':
            results['members'] = Member.objects.filter(
                Q(name__icontains=query) |
                Q(role__icontains=query) |
                Q(bio__icontains=query)
            )[:10]
        
        if category == 'all' or category == 'events':
            results['events'] = Event.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )[:10]
        
        if category == 'all' or category == 'achievements':
            results['achievements'] = Achievement.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )[:10]
        
        if category == 'all' or category == 'blog':
            results['blog_posts'] = BlogPost.objects.filter(
                status='published'
            ).filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__icontains=query)
            )[:10]
        
        if category == 'all' or category == 'projects':
            results['projects'] = Project.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(technologies__icontains=query)
            )[:10]
        
        if category == 'all' or category == 'resources':
            results['resources'] = Resource.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tags__icontains=query)
            )[:10]
    
    # Count total results
    total_results = sum(len(result_list) for result_list in results.values())
    
    context = {
        'form': form,
        'results': results,
        'total_results': total_results,
        'query': query,
        'category': category,
        'page_title': f'Search: {query}' if query else 'Search - NITER Computer Club'
    }
    return render(request, 'core/search.html', context)
