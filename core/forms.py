from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import (
    ContactSubmission, Newsletter, MembershipApplication, 
    BlogPost, FAQ, Project, Resource
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('subject', css_class='form-group mb-3'),
            Field('message', css_class='form-group mb-3'),
            Submit('submit', 'Send Message', css_class='btn btn-primary')
        )


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'd-flex gap-2'
        self.helper.layout = Layout(
            Field('email', css_class='flex-fill'),
            Submit('submit', 'Subscribe', css_class='btn btn-primary')
        )


class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            'full_name', 'email', 'phone', 'student_id', 'department', 
            'year_of_study', 'interested_segment', 'programming_languages',
            'experience_level', 'motivation', 'expectations'
        ]
        widgets = {
            'motivation': forms.Textarea(attrs={'rows': 4}),
            'expectations': forms.Textarea(attrs={'rows': 4}),
            'programming_languages': forms.TextInput(attrs={
                'placeholder': 'e.g., Python, JavaScript, Java, C++'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Personal Information
            '<h4 class="mb-3">Personal Information</h4>',
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('student_id', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('department', css_class='form-group col-md-6 mb-3'),
                Column('year_of_study', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            
            # Club Preferences
            '<h4 class="mb-3 mt-4">Club Preferences</h4>',
            Field('interested_segment', css_class='form-group mb-3'),
            Row(
                Column('programming_languages', css_class='form-group col-md-6 mb-3'),
                Column('experience_level', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('motivation', css_class='form-group mb-3'),
            Field('expectations', css_class='form-group mb-4'),
            
            Submit('submit', 'Submit Application', css_class='btn btn-primary btn-lg')
        )


class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('all', 'All Content'),
        ('members', 'Members'),
        ('events', 'Events'),
        ('achievements', 'Achievements'),
        ('blog', 'Blog Posts'),
        ('projects', 'Projects'),
        ('resources', 'Resources'),
    ]

    query = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search...',
            'class': 'form-control'
        }),
        required=True
    )
    category = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        required=False,
        initial='all',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'd-flex gap-2'
        self.helper.layout = Layout(
            Field('query', css_class='flex-fill'),
            Field('category'),
            Submit('submit', 'Search', css_class='btn btn-primary')
        )


# Admin Forms for enhanced content management
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'content', 'excerpt', 'featured_image',
            'status', 'tags', 'published_at'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 15}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-group mb-3'),
            Field('slug', css_class='form-group mb-3'),
            Field('excerpt', css_class='form-group mb-3'),
            Field('content', css_class='form-group mb-3'),
            Row(
                Column('status', css_class='form-group col-md-6 mb-3'),
                Column('published_at', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('tags', css_class='form-group mb-3'),
            Field('featured_image', css_class='form-group mb-4'),
            Submit('submit', 'Save Post', css_class='btn btn-primary')
        )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'technologies', 'github_url',
            'live_demo_url', 'image', 'status', 'segment',
            'team_members', 'start_date', 'completion_date'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
            'team_members': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-group mb-3'),
            Field('description', css_class='form-group mb-3'),
            Field('technologies', css_class='form-group mb-3'),
            Row(
                Column('github_url', css_class='form-group col-md-6 mb-3'),
                Column('live_demo_url', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-3'),
                Column('segment', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('start_date', css_class='form-group col-md-6 mb-3'),
                Column('completion_date', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('image', css_class='form-group mb-3'),
            Field('team_members', css_class='form-group mb-4'),
            Submit('submit', 'Save Project', css_class='btn btn-primary')
        )


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            'title', 'description', 'category', 'file',
            'external_url', 'tags', 'is_featured'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-group mb-3'),
            Field('description', css_class='form-group mb-3'),
            Row(
                Column('category', css_class='form-group col-md-6 mb-3'),
                Column('is_featured', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('file', css_class='form-group mb-3'),
            Field('external_url', css_class='form-group mb-3'),
            Field('tags', css_class='form-group mb-4'),
            Submit('submit', 'Save Resource', css_class='btn btn-primary')
        )