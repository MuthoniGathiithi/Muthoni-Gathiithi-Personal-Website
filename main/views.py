from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Project, Skill, Contact
from .forms import ContactForm

def home(request):
    """Home page with hero section and featured projects"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page with detailed information"""
    skills_by_category = {}
    skills = Skill.objects.all()
    
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'skills_by_category': skills_by_category,
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects page with filtering and pagination"""
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        projects_list = Project.objects.all()
    else:
        projects_list = Project.objects.filter(category=category)
    
    paginator = Paginator(projects_list, 6)  # Show 6 projects per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    
    # Get all categories for filter dropdown
    categories = Project.CATEGORY_CHOICES
    
    context = {
        'projects': projects,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, project_id):
    """Individual project detail page"""
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'main/project_detail.html', context)

def security_focus(request):
    """Security-focused projects and achievements"""
    security_projects = Project.objects.filter(category='security')
    
    # Security achievements and certifications
    security_achievements = [
        {
            'platform': 'TryHackMe',
            'profile': 'MuthoniGathiithi',
            'url': 'https://tryhackme.com/p/MuthoniGathiithi',
            'description': 'Cybersecurity learning platform'
        },
        {
            'platform': 'HackerRank',
            'profile': 'gathiithijoyce74',
            'url': 'https://www.hackerrank.com/profile/gathiithijoyce74',
            'description': 'Programming challenges and certifications'
        }
    ]
    
    context = {
        'security_projects': security_projects,
        'security_achievements': security_achievements,
    }
    return render(request, 'main/security.html', context)

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)

def api_projects(request):
    """API endpoint for projects (for AJAX loading)"""
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category=category)
    
    projects_data = []
    for project in projects:
        projects_data.append({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'category': project.get_category_display(),
            'github_url': project.github_url,
            'live_demo_url': project.live_demo_url,
            'technologies': project.technologies,
            'image': project.image.url if project.image else None,
        })
    
    return JsonResponse({'projects': projects_data})
