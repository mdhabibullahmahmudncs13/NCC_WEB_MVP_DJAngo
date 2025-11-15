from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
import random

from core.models import (
    Segment, Member, Achievement, GalleryPhoto, Event,
    ContactSubmission, Newsletter, BlogPost, FAQ, Project, 
    Resource, MembershipApplication
)


class Command(BaseCommand):
    help = 'Create sample data for the NCC website'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))
        
        # Create sample segments
        self.create_segments()
        
        # Create sample members
        self.create_members()
        
        # Create sample achievements
        self.create_achievements()
        
        # Create sample events
        self.create_events()
        
        # Create sample blog posts
        self.create_blog_posts()
        
        # Create sample projects
        self.create_projects()
        
        # Create sample resources
        self.create_resources()
        
        # Create sample FAQs
        self.create_faqs()
        
        # Create sample applications
        self.create_applications()
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))

    def create_segments(self):
        segments_data = [
            {
                'title': 'Web Development',
                'description': 'Full-stack web development using modern frameworks and technologies',
                'icon': '🌐',
                'founded': '2020',
                'vision': 'To create innovative web solutions that impact society',
                'mission': 'Developing cutting-edge web applications and training future developers',
                'activities': ['React.js Development', 'Django Development', 'API Design', 'UI/UX Design'],
                'achievements': ['10+ Web Projects', 'Industry Collaborations', 'Student Training Programs']
            },
            {
                'title': 'Machine Learning',
                'description': 'Artificial Intelligence and Machine Learning research and applications',
                'icon': '🤖',
                'founded': '2019',
                'vision': 'Advancing AI technology for sustainable development',
                'mission': 'Research and develop ML solutions for real-world problems',
                'activities': ['Deep Learning', 'Computer Vision', 'NLP', 'Data Science'],
                'achievements': ['Research Publications', 'ML Competitions', 'Industry Projects']
            },
            {
                'title': 'Mobile Development',
                'description': 'Cross-platform mobile application development',
                'icon': '📱',
                'founded': '2021',
                'vision': 'Creating mobile solutions for modern challenges',
                'mission': 'Developing innovative mobile applications for various platforms',
                'activities': ['Flutter Development', 'React Native', 'iOS Development', 'Android Development'],
                'achievements': ['20+ Mobile Apps', 'Play Store Publications', 'User Base Growth']
            },
            {
                'title': 'Cybersecurity',
                'description': 'Information security research and ethical hacking',
                'icon': '🔒',
                'founded': '2020',
                'vision': 'Securing digital infrastructure for a safer future',
                'mission': 'Educating about cybersecurity and developing secure systems',
                'activities': ['Penetration Testing', 'Security Audits', 'Awareness Programs', 'CTF Competitions'],
                'achievements': ['Security Certifications', 'CTF Winners', 'Bug Bounty Programs']
            }
        ]
        
        for data in segments_data:
            segment, created = Segment.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created segment: {segment.title}')

    def create_members(self):
        segments = list(Segment.objects.all())
        if not segments:
            return
            
        members_data = [
            {'name': 'Ahmed Rahman', 'role': 'President', 'position': 'Club Leader'},
            {'name': 'Fatima Khan', 'role': 'Vice President', 'position': 'Operations Manager'},
            {'name': 'Mohammad Ali', 'role': 'General Secretary', 'position': 'Administration'},
            {'name': 'Rashida Begum', 'role': 'Treasurer', 'position': 'Finance Manager'},
            {'name': 'Karim Uddin', 'role': 'Web Developer', 'position': 'Senior Developer'},
            {'name': 'Nasreen Akter', 'role': 'ML Engineer', 'position': 'Research Lead'},
            {'name': 'Ibrahim Hassan', 'role': 'Mobile Developer', 'position': 'App Development Lead'},
            {'name': 'Salma Khatun', 'role': 'Security Analyst', 'position': 'Cybersecurity Lead'},
            {'name': 'Rafiq Ahmed', 'role': 'Project Manager', 'position': 'Team Coordinator'},
            {'name': 'Amina Rahman', 'role': 'UI/UX Designer', 'position': 'Design Lead'},
            {'name': 'Tariq Islam', 'role': 'Backend Developer', 'position': 'System Architect'},
            {'name': 'Ruma Begum', 'role': 'Data Scientist', 'position': 'Analytics Lead'},
        ]
        
        for i, data in enumerate(members_data):
            member, created = Member.objects.get_or_create(
                name=data['name'],
                defaults={
                    **data,
                    'bio': f"Passionate technology enthusiast with expertise in {data['role'].lower()}. Dedicated to advancing technological innovation at NITER Computer Club.",
                    'email': f"{data['name'].lower().replace(' ', '.')}@nitercc.com",
                    'segment': segments[i % len(segments)],
                    'join_date': timezone.now().date() - timedelta(days=random.randint(30, 365)),
                    'skills': ['Programming', 'Leadership', 'Project Management', 'Technical Writing'],
                    'order': i
                }
            )
            if created:
                self.stdout.write(f'Created member: {member.name}')

    def create_achievements(self):
        achievements_data = [
            {
                'title': 'National Programming Contest Winners',
                'description': 'Our team secured 1st place in the National Programming Contest 2024',
                'category': 'competition',
                'date': timezone.now() - timedelta(days=30)
            },
            {
                'title': 'AI Research Paper Published',
                'description': 'Research paper on "Machine Learning for Sustainable Development" published in international journal',
                'category': 'academic',
                'date': timezone.now() - timedelta(days=60)
            },
            {
                'title': 'Mobile App Development Workshop',
                'description': 'Successfully conducted a 3-day mobile app development workshop with 100+ participants',
                'category': 'event',
                'date': timezone.now() - timedelta(days=15)
            },
            {
                'title': 'Industry Partnership with TechCorp',
                'description': 'Established strategic partnership with leading technology company for internships and projects',
                'category': 'recognition',
                'date': timezone.now() - timedelta(days=45)
            },
            {
                'title': 'Open Source Contribution Award',
                'description': 'Recognition for significant contributions to open source projects in the developer community',
                'category': 'project',
                'date': timezone.now() - timedelta(days=90)
            }
        ]
        
        for data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created achievement: {achievement.title}')

    def create_events(self):
        events_data = [
            {
                'title': 'Tech Innovation Summit 2024',
                'description': 'Annual technology summit featuring keynote speakers, workshops, and project showcases',
                'date': timezone.now() + timedelta(days=30),
                'location': 'NITER Auditorium',
                'status': 'upcoming'
            },
            {
                'title': 'Machine Learning Workshop Series',
                'description': 'Comprehensive ML workshop covering fundamentals to advanced topics',
                'date': timezone.now() + timedelta(days=15),
                'location': 'Computer Lab 1',
                'status': 'upcoming'
            },
            {
                'title': 'Hackathon 2024: Code for Good',
                'description': '48-hour hackathon focused on developing solutions for social problems',
                'date': timezone.now() - timedelta(days=30),
                'location': 'Innovation Center',
                'status': 'completed'
            },
            {
                'title': 'Cybersecurity Awareness Week',
                'description': 'Week-long program to raise awareness about cybersecurity best practices',
                'date': timezone.now() - timedelta(days=60),
                'location': 'Various Locations',
                'status': 'completed'
            },
            {
                'title': 'Web Development Bootcamp',
                'description': 'Intensive bootcamp covering modern web development technologies',
                'date': timezone.now() + timedelta(days=45),
                'location': 'Computer Lab 2',
                'status': 'upcoming'
            }
        ]
        
        for data in events_data:
            event, created = Event.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created event: {event.title}')

    def create_blog_posts(self):
        if not User.objects.exists():
            # Create a default user for blog posts
            user = User.objects.create_user(
                username='admin',
                email='admin@nitercc.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
        else:
            user = User.objects.first()
        
        posts_data = [
            {
                'title': 'Welcome to the New NCC Website',
                'slug': 'welcome-new-ncc-website',
                'content': '''We are excited to announce the launch of our new website! This platform will serve as the central hub for all NITER Computer Club activities, announcements, and resources.
                
The new website features:
- Modern, responsive design
- Project showcase
- Member profiles
- Event management
- Resource sharing
- News and updates

We invite all members and visitors to explore the new features and stay connected with our growing technology community.''',
                'excerpt': 'Announcing the launch of our new website with modern features and improved user experience.',
                'status': 'published',
                'tags': 'announcement,website,technology',
                'published_at': timezone.now() - timedelta(days=5)
            },
            {
                'title': 'Machine Learning Workshop Success',
                'slug': 'machine-learning-workshop-success',
                'content': '''Our recent Machine Learning Workshop was a tremendous success with over 80 participants from various departments. The workshop covered fundamental concepts, practical applications, and hands-on exercises.
                
Key highlights:
- Introduction to ML algorithms
- Python programming for ML
- Real-world case studies
- Hands-on projects
- Networking opportunities

We thank all participants and look forward to organizing more such educational events in the future.''',
                'excerpt': 'Recap of our successful Machine Learning Workshop with 80+ participants.',
                'status': 'published',
                'tags': 'workshop,machine-learning,education',
                'published_at': timezone.now() - timedelta(days=10)
            },
            {
                'title': 'Upcoming Hackathon: Code for Good',
                'slug': 'upcoming-hackathon-code-for-good',
                'content': '''We are organizing "Code for Good" - a 48-hour hackathon focused on developing technology solutions for social problems. This event aims to bring together creative minds to address real-world challenges.
                
Event Details:
- Duration: 48 hours
- Teams: 3-4 members
- Themes: Education, Healthcare, Environment, Social Welfare
- Prizes: Cash awards and internship opportunities
- Mentorship: Industry experts

Registration is now open. Don't miss this opportunity to make a positive impact through technology!''',
                'excerpt': 'Join our 48-hour hackathon focused on developing solutions for social problems.',
                'status': 'published',
                'tags': 'hackathon,social-impact,innovation',
                'published_at': timezone.now() - timedelta(days=15)
            }
        ]
        
        for data in posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=data['slug'],
                defaults={**data, 'author': user}
            )
            if created:
                self.stdout.write(f'Created blog post: {post.title}')

    def create_projects(self):
        segments = list(Segment.objects.all())
        members = list(Member.objects.all())
        
        if not segments:
            return
        
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-stack e-commerce solution built with Django and React, featuring user authentication, product management, and payment integration.',
                'technologies': 'Django, React, PostgreSQL, Redis, Docker',
                'github_url': 'https://github.com/nitercc/ecommerce',
                'status': 'completed',
                'start_date': timezone.now().date() - timedelta(days=180),
                'completion_date': timezone.now().date() - timedelta(days=30)
            },
            {
                'title': 'Student Management System',
                'description': 'Comprehensive student management system for educational institutions with features for attendance, grades, and communication.',
                'technologies': 'Python, Django, Bootstrap, MySQL',
                'github_url': 'https://github.com/nitercc/student-management',
                'status': 'completed',
                'start_date': timezone.now().date() - timedelta(days=120),
                'completion_date': timezone.now().date() - timedelta(days=15)
            },
            {
                'title': 'AI Chatbot Assistant',
                'description': 'Intelligent chatbot powered by natural language processing to assist students with academic queries and information.',
                'technologies': 'Python, TensorFlow, NLP, Flask, OpenAI API',
                'github_url': 'https://github.com/nitercc/ai-chatbot',
                'status': 'development',
                'start_date': timezone.now().date() - timedelta(days=60)
            },
            {
                'title': 'Mobile Learning App',
                'description': 'Cross-platform mobile application for interactive learning with offline capabilities and progress tracking.',
                'technologies': 'Flutter, Firebase, Dart, SQLite',
                'github_url': 'https://github.com/nitercc/learning-app',
                'live_demo_url': 'https://play.google.com/store/apps/details?id=com.nitercc.learning',
                'status': 'completed',
                'start_date': timezone.now().date() - timedelta(days=200),
                'completion_date': timezone.now().date() - timedelta(days=45)
            },
            {
                'title': 'Cybersecurity Training Platform',
                'description': 'Interactive platform for cybersecurity training with virtual labs and hands-on exercises.',
                'technologies': 'React, Node.js, Docker, Kubernetes, MongoDB',
                'github_url': 'https://github.com/nitercc/cybersec-training',
                'status': 'development',
                'start_date': timezone.now().date() - timedelta(days=90)
            }
        ]
        
        for i, data in enumerate(projects_data):
            project, created = Project.objects.get_or_create(
                title=data['title'],
                defaults={
                    **data,
                    'segment': segments[i % len(segments)]
                }
            )
            if created:
                # Add some team members
                project.team_members.set(random.sample(members, min(3, len(members))))
                self.stdout.write(f'Created project: {project.title}')

    def create_resources(self):
        resources_data = [
            {
                'title': 'Python Programming Guide',
                'description': 'Comprehensive guide to Python programming covering basics to advanced topics.',
                'category': 'tutorial',
                'external_url': 'https://docs.python.org/3/tutorial/',
                'tags': 'python,programming,tutorial',
                'is_featured': True
            },
            {
                'title': 'Web Development Cheat Sheet',
                'description': 'Quick reference guide for HTML, CSS, and JavaScript fundamentals.',
                'category': 'guide',
                'external_url': 'https://developer.mozilla.org/en-US/docs/Web',
                'tags': 'web-development,html,css,javascript',
                'is_featured': True
            },
            {
                'title': 'Machine Learning Algorithms',
                'description': 'Implementation examples of popular machine learning algorithms in Python.',
                'category': 'tutorial',
                'external_url': 'https://scikit-learn.org/stable/user_guide.html',
                'tags': 'machine-learning,algorithms,python',
                'is_featured': False
            },
            {
                'title': 'Git Version Control Guide',
                'description': 'Essential Git commands and workflows for collaborative development.',
                'category': 'guide',
                'external_url': 'https://git-scm.com/doc',
                'tags': 'git,version-control,collaboration',
                'is_featured': True
            },
            {
                'title': 'Database Design Principles',
                'description': 'Best practices for designing efficient and scalable databases.',
                'category': 'documentation',
                'external_url': 'https://www.postgresql.org/docs/',
                'tags': 'database,design,sql',
                'is_featured': False
            }
        ]
        
        for data in resources_data:
            resource, created = Resource.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created resource: {resource.title}')

    def create_faqs(self):
        faqs_data = [
            {
                'question': 'How can I join the NITER Computer Club?',
                'answer': 'You can join by filling out our membership application form available on the website. We welcome students from all departments who are interested in technology.',
                'category': 'membership',
                'order': 1
            },
            {
                'question': 'What programming languages do you teach?',
                'answer': 'We cover a wide range of programming languages including Python, JavaScript, Java, C++, and more. Our workshops are designed for both beginners and advanced learners.',
                'category': 'technical',
                'order': 2
            },
            {
                'question': 'Are there any membership fees?',
                'answer': 'No, membership is completely free. We believe in providing equal opportunities for all students to learn and grow in technology.',
                'category': 'membership',
                'order': 3
            },
            {
                'question': 'How often do you organize events?',
                'answer': 'We organize various events throughout the academic year including workshops, seminars, hackathons, and competitions. Usually, we have at least one major event per month.',
                'category': 'events',
                'order': 4
            },
            {
                'question': 'Can I contribute to club projects?',
                'answer': 'Absolutely! We encourage all members to participate in our ongoing projects. You can contribute based on your skill level and interests.',
                'category': 'general',
                'order': 5
            },
            {
                'question': 'Do you provide certificates for workshops?',
                'answer': 'Yes, we provide certificates of participation for all workshops and training programs. These certificates are recognized and can be valuable for your academic and professional portfolio.',
                'category': 'events',
                'order': 6
            }
        ]
        
        for data in faqs_data:
            faq, created = FAQ.objects.get_or_create(
                question=data['question'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created FAQ: {faq.question[:50]}...')

    def create_applications(self):
        segments = list(Segment.objects.all())
        if not segments:
            return
        
        applications_data = [
            {
                'full_name': 'Sarah Ahmed',
                'email': 'sarah.ahmed@example.com',
                'phone': '+880123456789',
                'student_id': 'CSE-2021-001',
                'department': 'Computer Science',
                'year_of_study': '3rd Year',
                'programming_languages': 'Python, Java, C++',
                'experience_level': 'Intermediate',
                'motivation': 'I want to enhance my programming skills and contribute to innovative projects.',
                'expectations': 'I expect to learn new technologies and collaborate with like-minded peers.',
                'status': 'pending'
            },
            {
                'full_name': 'Mohammad Rahman',
                'email': 'mohammad.rahman@example.com',
                'phone': '+880987654321',
                'student_id': 'EEE-2020-045',
                'department': 'Electrical Engineering',
                'year_of_study': '4th Year',
                'programming_languages': 'C, Python, MATLAB',
                'experience_level': 'Beginner',
                'motivation': 'To learn programming and explore technology applications in engineering.',
                'expectations': 'Gaining practical programming experience and networking opportunities.',
                'status': 'approved'
            }
        ]
        
        for i, data in enumerate(applications_data):
            application, created = MembershipApplication.objects.get_or_create(
                email=data['email'],
                defaults={
                    **data,
                    'interested_segment': segments[i % len(segments)],
                    'submitted_at': timezone.now() - timedelta(days=random.randint(1, 30))
                }
            )
            if created:
                self.stdout.write(f'Created application: {application.full_name}')