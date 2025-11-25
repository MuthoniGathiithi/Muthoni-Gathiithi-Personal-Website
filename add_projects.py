#!/usr/bin/env python
"""
Script to add all projects to the database
Run with: python manage.py shell < add_projects.py
Or use: python add_projects.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project

# List of all projects to add
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
        'technologies': 'Django, OpenCV, Arcface, Python, PostgreSQL',
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
        'description': 'An intelligent AI assistant designed to help students in virtual learning environments. Simplifies complex tasks and provides real-time assistance.',
        'category': 'security',
        'github_url': 'https://github.com/MuthoniGathiithi/VC_AI',
        'live_demo_url': '',
        'technologies': 'Python, AI, Machine Learning, Natural Language Processing',
        'featured': False,
    },
    {
        'title': 'Desktop AI Assistant',
        'description': 'Desktop automation AI assistant that automates routine tasks like file handling and opening tabs across Windows and Linux OS. Single-prompt operation.',
        'category': 'security',
        'github_url': 'https://github.com/MuthoniGathiithi/DesktopAI',
        'live_demo_url': '',
        'technologies': 'Python, Automation, AI, Cross-Platform, Desktop',
        'featured': False,
    },

    # Educational Projects - Flutter & Dart
    {
        'title': 'Beginner Dart Projects',
        'description': 'Collection of simple Dart coding tasks designed to build a strong foundation for Flutter app development. Perfect for beginners.',
        'category': 'educational',
        'github_url': 'https://github.com/MuthoniGathiithi/Begginer_dart_projects',
        'live_demo_url': '',
        'technologies': 'Dart, Flutter, Mobile Development, OOP',
        'featured': False,
    },
    {
        'title': 'Hello Flutter',
        'description': 'Flutter hello world application demonstrating the use of root widget, app bar widget, and text widget. Great starting point for Flutter beginners.',
        'category': 'educational',
        'github_url': 'https://github.com/MuthoniGathiithi/hello_Flutter-',
        'live_demo_url': '',
        'technologies': 'Flutter, Dart, Mobile Development, Widgets',
        'featured': False,
    },

    # Educational Projects - Python
    {
        'title': 'Python Basics',
        'description': 'Beginner-friendly repository showcasing foundational Python programming concepts. Organized folders with practical mini-projects and simple scripts.',
        'category': 'python',
        'github_url': 'https://github.com/MuthoniGathiithi/Python_Basics',
        'live_demo_url': '',
        'technologies': 'Python, Basics, Fundamentals, Scripts, Mini-Projects',
        'featured': False,
    },
    {
        'title': 'Python Beginner Projects',
        'description': 'Collection of simple Python scripts for absolute beginners. Covers printing, conditionals, input handling, and simple logic perfect for classroom exercises.',
        'category': 'python',
        'github_url': 'https://github.com/MuthoniGathiithi/Python_Begginer_Projects',
        'live_demo_url': '',
        'technologies': 'Python, Conditionals, Arithmetic, Variables, Functions',
        'featured': False,
    },
    {
        'title': '21 Python Projects',
        'description': 'Collection of 21 beginner-to-intermediate Python projects and practice scripts. Covers games, utilities, and small apps for hands-on learning.',
        'category': 'python',
        'github_url': 'https://github.com/MuthoniGathiithi/21_Python_project',
        'live_demo_url': '',
        'technologies': 'Python, Games, Utilities, SQLite, File Handling, Mini-Apps',
        'featured': False,
    },
    {
        'title': 'Python Arrays',
        'description': 'Project displaying practical applications of arrays across different coding tasks. Learn array manipulation and usage patterns.',
        'category': 'python',
        'github_url': 'https://github.com/MuthoniGathiithi/Python_Arrays',
        'live_demo_url': '',
        'technologies': 'Python, Arrays, Data Structures, Algorithms',
        'featured': False,
    },

    # Educational Projects - C++
    {
        'title': 'C++ Projects',
        'description': 'Wide variety of beginner-friendly C++ projects. Covers math operations, control flow, OOP, and data structures like arrays, vectors, stacks, and queues.',
        'category': 'cpp',
        'github_url': 'https://github.com/MuthoniGathiithi/C-_Plus_Plus_Projects-',
        'live_demo_url': '',
        'technologies': 'C++, OOP, Inheritance, Arrays, Vectors, Stacks, Queues, Algorithms',
        'featured': False,
    },
    {
        'title': 'Data Structures and Algorithms',
        'description': 'Beginner-friendly implementations of fundamental data structures and algorithms using C++. A practice ground for mastering core programming concepts.',
        'category': 'cpp',
        'github_url': 'https://github.com/MuthoniGathiithi/Data-Structures-and-Algorithims-',
        'live_demo_url': '',
        'technologies': 'C++, Data Structures, Algorithms, Problem Solving, Fundamentals',
        'featured': False,
    },

    # Other Educational Projects
    {
        'title': 'SmartBooks Web App',
        'description': 'Digital library web application for selling both e-books and physical books. PHP-based project with database and payment integration.',
        'category': 'educational',
        'github_url': 'https://github.com/MuthoniGathiithi/SmartBooks_web_app',
        'live_demo_url': '',
        'technologies': 'PHP, MySQL, HTML5, CSS3, JavaScript, E-commerce',
        'featured': False,
    },
    {
        'title': 'Personal Portfolio Platform',
        'description': 'This very portfolio — a tech-forward personal site that showcases 19 projects, security journeys, and contact channels in an interactive Django experience.',
        'category': 'django',
        'github_url': 'https://github.com/MuthoniGathiithi/Muthoni-Gathiithi-Personal-Website',
        'live_demo_url': '',
        'technologies': 'Django, Bootstrap 5, AOS, PostgreSQL',
        'featured': True,
    },
]

# Add projects to database
def add_projects():
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
            print(f"✓ Added: {project.title}")
        else:
            print(f"- Already exists: {project.title}")

if __name__ == '__main__':
    print("Adding projects to database...")
    add_projects()
    print("\nDone! All projects have been added successfully.")
