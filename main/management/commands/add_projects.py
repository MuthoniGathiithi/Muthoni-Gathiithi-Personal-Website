from django.core.management.base import BaseCommand
from main.models import Project


class Command(BaseCommand):
    help = 'Add all projects to the database'

    def handle(self, *args, **options):
        projects_data = [
            # Django Web Applications (Deployed on Render)
            {
                'title': 'Django Bug Report System',
                'description': 'A comprehensive bug tracking system built with Django. Allows users to report, track, and manage bugs with status updates and categorization.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/bug-report-system',
                'live_demo_url': 'https://django-bug-report-system.onrender.com',
                'technologies': 'Django, PostgreSQL, Bootstrap, JavaScript',
                'featured': True,
            },
            {
                'title': 'Facial Recognition System',
                'description': 'Advanced facial recognition system using OpenCV and Arcface for facial detection, feature extraction, and matching. Production-ready Django application.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/identiface',
                'live_demo_url': 'https://facial-recognition-3899.onrender.com',
                'technologies': 'Django, OpenCV, Arcface, Python, PostgreSQL, Facial Detection',
                'featured': True,
            },
            {
                'title': 'Admin Portal',
                'description': 'Full-featured admin dashboard for managing users, permissions, and system settings. Complete CRUD operations with role-based access control.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/admin-portal',
                'live_demo_url': 'https://admin-portal-xxlt.onrender.com',
                'technologies': 'Django, PostgreSQL, Bootstrap, JavaScript, AJAX',
                'featured': True,
            },
            {
                'title': 'To-Do App',
                'description': 'Simple yet powerful task management application. Create, update, delete, and organize your tasks with priority levels and due dates.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/todo-app',
                'live_demo_url': 'https://to-do-app-r38f.onrender.com',
                'technologies': 'Django, SQLite, HTML5, CSS3, JavaScript',
                'featured': False,
            },
            {
                'title': 'Django Attendance System',
                'description': 'Automated attendance tracking system for educational institutions. Track attendance, generate reports, and manage student records efficiently.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/attendance-system',
                'live_demo_url': 'https://djnago-attendance-sytem.onrender.com',
                'technologies': 'Django, PostgreSQL, Bootstrap, Python, Charts.js',
                'featured': False,
            },
            {
                'title': 'Django Authentication System',
                'description': 'Complete authentication and authorization system with email verification, password reset, and two-factor authentication. Production-ready solution.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/django-auth-system',
                'live_demo_url': 'https://django-full-authentication-system.onrender.com',
                'technologies': 'Django, JWT, PostgreSQL, Email, Security',
                'featured': False,
            },
            {
                'title': 'Contact Book App',
                'description': 'Feature-rich contact management application. Store, search, and manage contacts with advanced filtering and organization capabilities.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/contact-book',
                'live_demo_url': 'https://django-contact-book-app.onrender.com',
                'technologies': 'Django, PostgreSQL, Bootstrap, JavaScript, Export',
                'featured': False,
            },
            # Security/AI Projects
            {
                'title': 'Virtual Campus AI',
                'description': 'An intelligent AI assistant designed to assist students using virtual learning in simple tasks. Provides real-time support and automation.',
                'category': 'security',
                'github_url': 'https://github.com/MuthoniGathiithi/VC_AI',
                'live_demo_url': '',
                'technologies': 'Python, AI, Machine Learning, Natural Language Processing, Automation',
                'featured': False,
            },
            {
                'title': 'Desktop AI Assistant',
                'description': 'A desktop AI assistant designed to automate routine tasks such as file handling, opening tabs, and more - all in a SINGLE prompt. Works on Windows and Linux OS.',
                'category': 'security',
                'github_url': 'https://github.com/MuthoniGathiithi/DesktopAI',
                'live_demo_url': '',
                'technologies': 'Python, Automation, AI, Cross-Platform, Desktop Automation',
                'featured': False,
            },
            # Educational Projects - Flutter & Dart
            {
                'title': 'Beginner Dart Projects',
                'description': 'Simple dart coding tasks designed to build a strong foundation for Flutter app development. Perfect for beginners learning mobile development.',
                'category': 'educational',
                'github_url': 'https://github.com/MuthoniGathiithi/Begginer_dart_projects',
                'live_demo_url': '',
                'technologies': 'Dart, Flutter, Mobile Development, OOP, Widgets',
                'featured': False,
            },
            {
                'title': 'Hello Flutter',
                'description': 'A Flutter hello world app demonstrating the use of root widget, app bar widget, and text widget. Great starting point for Flutter beginners.',
                'category': 'educational',
                'github_url': 'https://github.com/MuthoniGathiithi/hello_Flutter-',
                'live_demo_url': '',
                'technologies': 'Flutter, Dart, Mobile Development, Widgets',
                'featured': False,
            },
            # Educational Projects - Python
            {
                'title': 'Python Basics',
                'description': 'A beginner-friendly repository created to showcase foundational Python programming concepts. Contains organized folders with practical mini-projects and simple scripts.',
                'category': 'python',
                'github_url': 'https://github.com/MuthoniGathiithi/Python_Basics',
                'live_demo_url': '',
                'technologies': 'Python, Basics, Fundamentals, Scripts, Mini-Projects, OOP',
                'featured': False,
            },
            {
                'title': 'Python Beginner Projects',
                'description': 'A collection of simple Python scripts designed to help absolute beginners practice core programming concepts. Covers printing, conditionals, input handling, and simple logic.',
                'category': 'python',
                'github_url': 'https://github.com/MuthoniGathiithi/Python_Begginer_Projects',
                'live_demo_url': '',
                'technologies': 'Python, Conditionals, Arithmetic, Variables, Functions, Input/Output',
                'featured': False,
            },
            {
                'title': '21 Python Projects',
                'description': 'A collection of beginner-to-intermediate Python projects and practice scripts covering core programming concepts, games, utilities, and small apps.',
                'category': 'python',
                'github_url': 'https://github.com/MuthoniGathiithi/21_Python_project',
                'live_demo_url': '',
                'technologies': 'Python, Games, Utilities, SQLite, File Handling, Mini-Apps, Data Structures',
                'featured': False,
            },
            {
                'title': 'Python Arrays',
                'description': 'A project displaying the use of arrays across different coding tasks. Learn array manipulation and practical usage patterns.',
                'category': 'python',
                'github_url': 'https://github.com/MuthoniGathiithi/Python_Arrays',
                'live_demo_url': '',
                'technologies': 'Python, Arrays, Data Structures, Algorithms, List Operations',
                'featured': False,
            },
            # Educational Projects - C++
            {
                'title': 'C++ Projects',
                'description': 'A wide variety of beginner-friendly C++ projects designed to help you master core programming concepts. Covers math operations, control flow, OOP, arrays, vectors, stacks, and queues.',
                'category': 'cpp',
                'github_url': 'https://github.com/MuthoniGathiithi/C-_Plus_Plus_Projects-',
                'live_demo_url': '',
                'technologies': 'C++, OOP, Inheritance, Arrays, Vectors, Stacks, Queues, Algorithms, Classes',
                'featured': False,
            },
            {
                'title': 'Data Structures and Algorithms',
                'description': 'Beginner-friendly implementations of fundamental data structures and algorithms using C++. Serves as a practice ground for mastering core programming concepts and algorithmic thinking.',
                'category': 'cpp',
                'github_url': 'https://github.com/MuthoniGathiithi/Data-Structures-and-Algorithims-',
                'live_demo_url': '',
                'technologies': 'C++, Data Structures, Algorithms, Problem Solving, Fundamentals, Implementation',
                'featured': False,
            },
            # Other Educational Projects
            {
                'title': 'SmartBooks Web App',
                'description': 'A PHP project of a digital library for selling both e-books and physical books. Full-featured e-commerce platform for book management.',
                'category': 'educational',
                'github_url': 'https://github.com/MuthoniGathiithi/SmartBooks_web_app',
                'live_demo_url': '',
                'technologies': 'PHP, MySQL, HTML5, CSS3, JavaScript, E-commerce, Database Design',
                'featured': False,
            },
            {
                'title': 'Personal Portfolio Platform',
                'description': 'Tech-inspired Django portfolio aggregating 19 projects, security badges, and collaboration links.',
                'category': 'django',
                'github_url': 'https://github.com/MuthoniGathiithi/Muthoni-Gathiithi-Personal-Website',
                'live_demo_url': '',
                'technologies': 'Django, Bootstrap 5, AOS, PostgreSQL',
                'featured': True,
            },
        ]

        # Add projects to database
        added_count = 0
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'category': project_data['category'],
                    'github_url': project_data['github_url'],
                    'live_demo_url': project_data['live_demo_url'],
                    'technologies': project_data['technologies'],
                    'featured': project_data['featured'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"✓ Added: {project.title}"))
                added_count += 1
            else:
                self.stdout.write(self.style.WARNING(f"- Already exists: {project.title}"))

        self.stdout.write(self.style.SUCCESS(f"\nDone! {added_count} new projects added successfully."))
