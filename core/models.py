from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import json


class Segment(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    icon = models.CharField(max_length=255, blank=True, help_text="Emoji or icon")
    photo = models.ImageField(upload_to='segments/', blank=True, null=True)
    founded = models.CharField(max_length=100, blank=True)
    activities = models.JSONField(default=list, blank=True, help_text="List of activities")
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    achievements = models.JSONField(default=list, blank=True, help_text="List of achievements")
    contact = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('segment_detail', kwargs={'pk': self.pk})

    @property
    def activities_list(self):
        """Return activities as a list"""
        if isinstance(self.activities, str):
            try:
                return json.loads(self.activities)
            except json.JSONDecodeError:
                return []
        return self.activities or []

    @property
    def achievements_list(self):
        """Return achievements as a list"""
        if isinstance(self.achievements, str):
            try:
                return json.loads(self.achievements)
            except json.JSONDecodeError:
                return []
        return self.achievements or []


class Member(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    skills = models.JSONField(default=list, blank=True, help_text="List of skills")
    join_date = models.DateField(blank=True, null=True)
    segment = models.ForeignKey(Segment, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"

    @property
    def skills_list(self):
        """Return skills as a list"""
        if isinstance(self.skills, str):
            try:
                return json.loads(self.skills)
            except json.JSONDecodeError:
                return []
        return self.skills or []


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('competition', 'Competition'),
        ('project', 'Project'),
        ('recognition', 'Recognition'),
        ('event', 'Event'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('achievement_detail', kwargs={'pk': self.pk})


class GalleryPhoto(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('meeting', 'Meeting'),
        ('project', 'Project'),
        ('workshop', 'Workshop'),
        ('competition', 'Competition'),
        ('general', 'General'),
    ]

    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=500)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Gallery: {self.caption[:50]}"


class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})


class ContactSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('membership', 'Membership'),
        ('collaboration', 'Collaboration'),
        ('technical', 'Technical Support'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, help_text="Brief description for previews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def tags_list(self):
        """Return tags as a list"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('membership', 'Membership'),
        ('events', 'Events'),
        ('technical', 'Technical'),
        ('segments', 'Segments'),
    ]

    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'question']

    def __str__(self):
        return self.question[:100]


class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('development', 'In Development'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Technologies used (comma-separated)")
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    segment = models.ForeignKey(Segment, on_delete=models.SET_NULL, blank=True, null=True, related_name='projects')
    team_members = models.ManyToManyField(Member, blank=True, related_name='projects')
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    @property
    def technologies_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('tutorial', 'Tutorial'),
        ('documentation', 'Documentation'),
        ('template', 'Template'),
        ('tool', 'Tool'),
        ('guide', 'Guide'),
        ('presentation', 'Presentation'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    external_url = models.URLField(blank=True, help_text="External link if not uploading a file")
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    downloads = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.pk})

    @property
    def tags_list(self):
        """Return tags as a list"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class MembershipApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('interview', 'Interview Scheduled'),
    ]

    # Personal Information
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    student_id = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=20)
    
    # Preferences
    interested_segment = models.ForeignKey(Segment, on_delete=models.SET_NULL, null=True, blank=True)
    programming_languages = models.CharField(max_length=500, help_text="Programming languages known")
    experience_level = models.CharField(max_length=100)
    motivation = models.TextField(help_text="Why do you want to join?")
    expectations = models.TextField(help_text="What do you expect from the club?")
    
    # Administrative
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_applications')
    review_notes = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} - {self.get_status_display()}"
