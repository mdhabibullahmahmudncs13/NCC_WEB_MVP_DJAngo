# NITER Computer Club - Django Website

A Django recreation of the NITER Computer Club website, originally built with Next.js and Appwrite. This project provides a comprehensive club management system with member profiles, segments, achievements, gallery, and events.

## 🌟 Features

### 🏠 **Homepage**
- Modern hero section with club introduction
- Interactive segment cards with hover effects
- Quick navigation to all major sections
- Responsive Bootstrap design

### 🎯 **Segment System**
- **Individual Segment Pages**: Rich segment profiles with detailed information
- **Member Management**: Add, edit, and manage segment-specific members
- **Rich Content**: Vision, mission, activities, achievements
- **Visual Elements**: Header photos, member profile pictures
- **Admin Controls**: Full CRUD operations through Django admin

### 👥 **Member Management**
- **Enhanced Profiles**: Name, role, position, bio, skills, join date
- **Photo Support**: Profile picture uploads and management
- **Segment Assignment**: Members can be assigned to specific segments
- **Skill Tracking**: JSON field for technical skills
- **Contact Information**: Email addresses and professional details

### 🏆 **Achievements**
- **Achievement Gallery**: Showcase club accomplishments
- **Rich Media**: Images, descriptions, dates, categories
- **Admin Management**: Create, edit, delete achievements through Django admin
- **Professional Display**: Card-based achievement showcase

### 📸 **Photo Gallery**
- **Image Management**: Upload and organize club photos
- **Category System**: Organize photos by events, projects, etc.
- **Responsive Grid**: Beautiful photo grid layout
- **Admin Controls**: Full photo management through Django admin

### 🎉 **Events**
- **Event Management**: Create and manage club events
- **Rich Details**: Date, location, description, photos, status
- **Event Status**: Upcoming, ongoing, completed, cancelled
- **Visual Timeline**: Professional event display

### 🔐 **Admin Interface**
- **Django Admin**: Enhanced admin interface with custom forms
- **Admin Dashboard**: Statistics overview and quick actions
- **User Management**: Built-in Django user authentication
- **Media Management**: File upload handling for photos
- **CRUD Operations**: Complete content management

## 🛠 Technology Stack

### **Backend**
- **Django 5.2.8** - Python web framework
- **SQLite** - Database (easily configurable to PostgreSQL/MySQL)
- **Pillow** - Image processing
- **Python Decouple** - Environment configuration

### **Frontend**
- **Bootstrap 5.3** - CSS framework
- **Bootstrap Icons** - Icon library
- **Django Templates** - Server-side rendering
- **Custom CSS** - Tailored styling matching original design

### **Development**
- **Django Admin** - Built-in admin interface
- **Django Forms** - Form handling with Crispy Forms
- **Static Files** - CSS, JavaScript, and image management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Clone and Setup
```bash
# Navigate to the project directory
cd path/to/NCC_D

# Activate virtual environment (if not already activated)
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies (already installed)
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
# Or use existing: username=admin, password=admin123
```

### 3. Run Development Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### 4. Admin Access
- Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Admin Dashboard: [http://127.0.0.1:8000/admin/dashboard/](http://127.0.0.1:8000/admin/dashboard/)
- **Username**: admin
- **Password**: admin123

## 📁 Project Structure

```
NCC_D/
├── ncc_website/                 # Django project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── core/                       # Main Django app
│   ├── models.py               # Database models
│   ├── views.py                # View functions and classes
│   ├── admin.py                # Django admin configuration
│   ├── urls.py                 # App URL patterns
│   └── migrations/             # Database migrations
├── templates/                  # Django templates
│   ├── base.html               # Base template with navigation
│   ├── core/                   # Core app templates
│   │   ├── home.html           # Homepage
│   │   ├── about.html          # About page
│   │   ├── members.html        # Members listing
│   │   ├── segments.html       # Segments listing
│   │   ├── achievements.html   # Achievements gallery
│   │   └── ...
│   └── admin/                  # Admin templates
│       └── dashboard.html      # Admin dashboard
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── img/
│       └── ncc-logo.svg       # Club logo
├── media/                      # User uploaded files
└── manage.py                   # Django management script
```

## 🔧 Database Schema

### **Models Overview**

#### **Segment Model**
```python
class Segment(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    icon = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='segments/', blank=True, null=True)
    founded = models.CharField(max_length=100, blank=True)
    activities = models.JSONField(default=list, blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    achievements = models.JSONField(default=list, blank=True)
    contact = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### **Member Model**
```python
class Member(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    skills = models.JSONField(default=list, blank=True)
    join_date = models.DateField(blank=True, null=True)
    segment = models.ForeignKey(Segment, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### **Other Models**
- **Achievement**: Club accomplishments with images and categories
- **GalleryPhoto**: Photo collection with captions and categories  
- **Event**: Club events with dates, locations, and status

## 🎨 Customization

### **Styling**
- Modify `static/css/style.css` for custom styles
- Bootstrap 5 classes available throughout templates
- Responsive design with mobile-first approach

### **Content**
- Update club information in templates
- Modify homepage content in `templates/core/home.html`
- Customize navigation in `templates/base.html`

### **Features**
- Add new pages by creating views and templates
- Extend models in `core/models.py`
- Customize admin interface in `core/admin.py`

## 👨‍💼 Admin Features

### **Enhanced Admin Interface**
- **Rich Admin**: Custom admin views with image previews
- **Quick Actions**: Direct links to add/edit content
- **Statistics Dashboard**: Overview of all content
- **Bulk Operations**: Manage multiple items efficiently

### **Content Management**
1. **Segments**: Create and manage specialized focus areas
2. **Members**: Add team members with photos and details
3. **Achievements**: Showcase accomplishments with images
4. **Gallery**: Upload and organize photos
5. **Events**: Manage upcoming and past events

### **User Management**
- Built-in Django user authentication
- Staff and superuser permissions
- Secure admin access

## 🚀 Deployment

### **Production Setup**
1. **Environment Variables**
   ```bash
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Database Configuration**
   - Configure PostgreSQL or MySQL for production
   - Update `DATABASES` setting in settings.py

3. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Media Files**
   - Configure media file serving for production
   - Consider using cloud storage (AWS S3, etc.)

### **Deployment Platforms**
- **Heroku**: Easy Django deployment
- **DigitalOcean**: VPS with more control
- **PythonAnywhere**: Python-focused hosting
- **Railway**: Modern deployment platform

## 🔄 Migration from Next.js/Appwrite

### **Key Differences**
1. **Backend**: Appwrite → Django with SQLite/PostgreSQL
2. **Frontend**: React → Django Templates with Bootstrap
3. **Authentication**: Appwrite Auth → Django Built-in Auth
4. **File Storage**: Appwrite Storage → Django Media Files
5. **Database**: Appwrite Database → Django ORM

### **Data Migration**
If migrating from existing Appwrite data:
1. Export data from Appwrite collections
2. Create Django management commands to import data
3. Map Appwrite document structure to Django models
4. Handle file migrations for uploaded images

## 📊 Performance & SEO

### **Optimizations**
- **Django ORM**: Efficient database queries with select_related/prefetch_related
- **Image Optimization**: Pillow for image processing
- **Static Files**: Efficient serving with Django's static file handling
- **Caching**: Django's caching framework ready for implementation

### **SEO Features**
- **Meta Tags**: Proper title and description tags
- **Semantic HTML**: Clean, accessible markup
- **Responsive Design**: Mobile-friendly layouts
- **Fast Loading**: Optimized CSS and images

## 🧪 Testing

### **Manual Testing**
1. Test public pages (home, about, segments, members, achievements, gallery, events)
2. Test admin authentication and dashboard
3. Test CRUD operations through admin interface
4. Verify image uploads and display
5. Test responsive design on different screen sizes

### **Development Testing**
```bash
# Run Django's built-in tests
python manage.py test

# Check for issues
python manage.py check
```

## 🤝 Contributing

### **Development Guidelines**
1. Follow Django best practices
2. Use Python PEP 8 style guide
3. Write descriptive commit messages
4. Test changes thoroughly before committing

### **Adding Features**
1. Create new views in `core/views.py`
2. Add URL patterns to `core/urls.py`
3. Create templates in `templates/core/`
4. Update models if needed with migrations

## 📚 Documentation

- **Django Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com/)
- **Bootstrap Documentation**: [getbootstrap.com](https://getbootstrap.com/)
- **Model Reference**: See `core/models.py` for data structure
- **View Reference**: See `core/views.py` for functionality

## 🔧 Environment Configuration

### **Required Environment Variables**
```bash
DEBUG=True                    # Development mode
SECRET_KEY=your-secret-key   # Django secret key
ALLOWED_HOSTS=localhost      # Allowed hosts
```

### **Optional Configuration**
- Database URL for production databases
- Email configuration for contact forms
- Cloud storage settings for media files

## 📞 Support & Contact

**NITER Computer Club**
- **Website**: Running on Django!
- **Email**: computerclubniter@gmail.com
- **Admin Access**: /admin/ (Django Admin Panel)

**Development Team**
- **Framework**: Django 5.2.8
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5 + Django Templates

---

## 🎯 Key Achievements

✅ **Complete Migration**: Successfully migrated from Next.js/Appwrite to Django
✅ **Feature Parity**: All original features implemented and working
✅ **Enhanced Admin**: Rich Django admin interface with dashboard
✅ **Responsive Design**: Mobile-friendly Bootstrap implementation
✅ **SEO Optimized**: Proper meta tags and semantic HTML
✅ **Production Ready**: Configurable for deployment

**Built with ❤️ using Django by the NITER Computer Club Development Team**

*Advancing technological excellence through robust web development and innovative Django solutions*