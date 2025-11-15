from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import (
    Segment, Member, Achievement, GalleryPhoto, Event,
    ContactSubmission, Newsletter, BlogPost, FAQ, Project, 
    Resource, MembershipApplication
)


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'photo_preview', 'founded', 'member_count', 'created_at']
    list_filter = ['created_at', 'founded']
    search_fields = ['title', 'description', 'vision', 'mission']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'description', 'icon', 'photo']
        }),
        ('Details', {
            'fields': ['founded', 'vision', 'mission', 'contact']
        }),
        ('Activities & Achievements', {
            'fields': ['activities', 'achievements'],
            'classes': ['collapse']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;"/>', obj.photo.url)
        return "No photo"
    photo_preview.short_description = "Photo"

    def member_count(self, obj):
        return obj.members.count()
    member_count.short_description = "Members"


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'segment', 'photo_preview', 'join_date', 'order']
    list_filter = ['segment', 'role', 'join_date', 'created_at']
    search_fields = ['name', 'role', 'email', 'bio']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['name', 'role', 'position', 'email', 'photo']
        }),
        ('Details', {
            'fields': ['bio', 'skills', 'join_date', 'segment']
        }),
        ('Display', {
            'fields': ['order']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;"/>', obj.photo.url)
        return "No photo"
    photo_preview.short_description = "Photo"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date', 'image_preview', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'category', 'date', 'image']
        }),
        ('Description', {
            'fields': ['description']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 3px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = "Image"


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['caption_short', 'category', 'image_preview', 'uploaded_at']
    list_filter = ['category', 'uploaded_at']
    search_fields = ['caption']
    readonly_fields = ['uploaded_at']
    
    def caption_short(self, obj):
        return obj.caption[:50] + "..." if len(obj.caption) > 50 else obj.caption
    caption_short.short_description = "Caption"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 3px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = "Photo"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'status', 'image_preview', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['title', 'description', 'location']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'date', 'location', 'status', 'image']
        }),
        ('Description', {
            'fields': ['description']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 3px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = "Image"


# Customize admin site
admin.site.site_header = "NITER Computer Club Admin"
admin.site.site_title = "NCC Admin"
admin.site.index_title = "Welcome to NCC Administration"


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['subject', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    
    fieldsets = [
        ('Contact Information', {
            'fields': ['name', 'email', 'subject', 'created_at']
        }),
        ('Message', {
            'fields': ['message']
        }),
        ('Admin', {
            'fields': ['is_read', 'admin_notes']
        }),
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at']
    list_editable = ['is_active']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'published_at', 'created_at']
    list_filter = ['status', 'author', 'published_at', 'created_at']
    search_fields = ['title', 'content', 'tags']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    
    fieldsets = [
        ('Content', {
            'fields': ['title', 'slug', 'excerpt', 'content']
        }),
        ('Metadata', {
            'fields': ['author', 'status', 'tags', 'featured_image']
        }),
        ('Publishing', {
            'fields': ['published_at']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        if obj.status == 'published' and not obj.published_at:
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_short', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['question', 'answer']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['order', 'is_active']
    
    fieldsets = [
        ('Content', {
            'fields': ['question', 'answer', 'category']
        }),
        ('Display', {
            'fields': ['order', 'is_active']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def question_short(self, obj):
        return obj.question[:70] + "..." if len(obj.question) > 70 else obj.question
    question_short.short_description = "Question"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'segment', 'start_date', 'completion_date', 'image_preview']
    list_filter = ['status', 'segment', 'start_date', 'completion_date']
    search_fields = ['title', 'description', 'technologies']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['team_members']
    date_hierarchy = 'start_date'
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'description', 'image']
        }),
        ('Technical Details', {
            'fields': ['technologies', 'github_url', 'live_demo_url']
        }),
        ('Project Management', {
            'fields': ['status', 'segment', 'team_members']
        }),
        ('Timeline', {
            'fields': ['start_date', 'completion_date']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 3px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = "Image"


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'downloads', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'tags']
    readonly_fields = ['created_at', 'updated_at', 'downloads']
    list_editable = ['is_featured']
    
    fieldsets = [
        ('Content', {
            'fields': ['title', 'description', 'category']
        }),
        ('Files & Links', {
            'fields': ['file', 'external_url']
        }),
        ('Metadata', {
            'fields': ['tags', 'is_featured']
        }),
        ('Statistics', {
            'fields': ['downloads'],
            'classes': ['collapse']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'status', 'interested_segment', 'submitted_at']
    list_filter = ['status', 'interested_segment', 'department', 'submitted_at']
    search_fields = ['full_name', 'email', 'student_id', 'department']
    readonly_fields = ['submitted_at', 'reviewed_at']
    list_editable = ['status']
    
    fieldsets = [
        ('Personal Information', {
            'fields': ['full_name', 'email', 'phone', 'student_id', 'department', 'year_of_study']
        }),
        ('Club Preferences', {
            'fields': ['interested_segment', 'programming_languages', 'experience_level']
        }),
        ('Motivation', {
            'fields': ['motivation', 'expectations']
        }),
        ('Administrative', {
            'fields': ['status', 'reviewed_by', 'review_notes', 'submitted_at', 'reviewed_at']
        }),
    ]

    def save_model(self, request, obj, form, change):
        if 'status' in form.changed_data and obj.status != 'pending':
            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()
        super().save_model(request, obj, form, change)
