# Portfolio Website - Adding Projects Guide

This guide explains how to add all the projects to your Django portfolio website.

## Quick Setup

There are two ways to add the projects:

### Method 1: Using Django Management Command (Recommended)

```bash
# Make sure you're in the project directory
cd /home/muthoni/Muthoni-Gathiithi-Personal-Website

# Run the management command
python3 manage.py add_projects
```

### Method 2: Using the Direct Python Script

```bash
# Make sure you're in the project directory
cd /home/muthoni/Muthoni-Gathiithi-Personal-Website

# Run the insertion script
python3 insert_projects.py
```

## Projects Being Added

### Django Web Applications (7 projects - deployed on Render)
1. **Django Bug Report System** - Bug tracking with status updates
2. **Facial Recognition System** - OpenCV & Arcface integration
3. **Admin Portal** - User and permission management dashboard
4. **To-Do App** - Task management application
5. **Django Attendance System** - Educational institution attendance tracking
6. **Django Authentication System** - Complete auth with email & 2FA
7. **Contact Book App** - Contact management application

### Security/AI Projects (2 projects)
1. **Virtual Campus AI** - AI assistant for virtual learning
2. **Desktop AI Assistant** - Desktop automation with single-prompt operation

### Educational Projects (12 projects)
1. **Beginner Dart Projects** - Foundation for Flutter development
2. **Hello Flutter** - Flutter hello world application
3. **Python Basics** - Foundational Python concepts
4. **Python Beginner Projects** - Simple scripts for beginners
5. **21 Python Projects** - Beginner-to-intermediate collection
6. **Python Arrays** - Array applications in coding
7. **C++ Projects** - Beginner C++ projects with OOP
8. **Data Structures and Algorithms** - C++ implementations
9. **SmartBooks Web App** - Digital library PHP application

## Website Features Now Include

✅ **Navigation Bar**
- Home, About, Projects (with category filters)
- Security Focus section
- Connect dropdown (Email, LinkedIn, GitHub)

✅ **Footer with All Social Links**
- Email: gathiithijoyce74@gmail.com
- LinkedIn: /in/muthoni-gathiithi
- GitHub: /MuthoniGathiithi
- HackerRank: gathiithijoyce74
- TryHackMe: MuthoniGathiithi

✅ **Project Categories**
- Django Applications
- Security Projects
- Educational Content
- C++ Projects
- Python Scripts

✅ **Enhanced Home Page**
- View My Portfolio button
- GitHub Profile link
- Get In Touch button
- Featured projects showcase
- Specializations section

## Project Structure

```
Projects are organized by category:
- django: Web applications with live demos
- security: Security and AI projects
- educational: Learning-focused repositories
- cpp: C++ projects
- python: Python scripts and tutorials
```

## Database Integration

All projects are stored in the `Project` model with:
- Title
- Description
- Category
- GitHub URL
- Live Demo URL (where applicable)
- Technologies used
- Featured flag (for homepage showcase)

## Next Steps

1. Run the project insertion command
2. Access Django admin at `/admin/` to verify projects
3. View projects on the homepage and projects page
4. Test all links are working correctly

## Troubleshooting

If you encounter issues:

1. **ModuleNotFoundError**: Install requirements: `pip3 install -r requirements.txt`
2. **Database issues**: Run migrations first: `python3 manage.py migrate`
3. **Permission errors**: Ensure you're in the correct directory and have file permissions

## Support

For questions or issues, contact: gathiithijoyce74@gmail.com
