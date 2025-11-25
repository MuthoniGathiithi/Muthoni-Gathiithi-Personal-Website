from collections import Counter, defaultdict

from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import ContactForm
from .models import Contact, Project, Skill


def _tech_stack_list(project):
    return [tech.strip() for tech in project.technologies.split(',') if tech.strip()]


def _category_lookup():
    return {key: label for key, label in Project.CATEGORY_CHOICES}


def _featured_projects():
    """Ensure featured cards highlight different focus areas."""
    projects = Project.objects.all()
    featured = []
    used_ids = set()
    priority_order = ['django', 'security', 'python', 'cpp', 'educational']

    for category in priority_order:
        project = projects.filter(category=category).order_by('-featured', '-created_date').first()
        if project and project.id not in used_ids:
            featured.append(project)
            used_ids.add(project.id)

    if len(featured) < 4:
        extras = projects.exclude(id__in=used_ids).order_by('-featured', '-created_date')[: 4 - len(featured)]
        featured.extend(extras)

    return featured

def home(request):
    """Home page with hero section and featured projects"""
    featured_projects = _featured_projects()
    projects = Project.objects.all()

    tech_counter = Counter()
    render_projects = 0
    category_totals = projects.values('category').annotate(total=Count('id'))
    category_lookup = _category_lookup()

    for project in projects:
        tech_counter.update(_tech_stack_list(project))
        if project.live_demo_url:
            render_projects += 1

    project_metrics = {
        'total': projects.count(),
        'render': render_projects,
        'security': projects.filter(category='security').count(),
        'educational': projects.filter(category='educational').count() + projects.filter(category='python').count(),
    }

    specialization_copy = {
        'django': 'Production-ready Django systems that ship with authentication, dashboards, and analytics.',
        'security': 'Automation assistants and security tooling inspired by TryHackMe and HackerRank drills.',
        'python': 'Hands-on Python repositories that reinforce data handling, logic, and automation.',
        'cpp': 'C++ practice grounds covering DS&A, OOP, and performance-focused patterns.',
        'educational': 'Learning accelerators for Dart, Flutter, PHP, and cross-language fundamentals.',
    }

    category_projects = defaultdict(list)
    for project in projects:
        category_projects[project.category].append(project.title)

    specializations = []
    for key in ['django', 'security', 'python', 'cpp', 'educational']:
        project_titles = category_projects.get(key, [])[:3]
        if not project_titles:
            continue
        specializations.append(
            {
                'title': category_lookup.get(key, key),
                'description': specialization_copy.get(key, ''),
                'count': len(category_projects.get(key, [])),
                'projects': project_titles,
            }
        )

    stack_snapshot = [{'name': name, 'count': count} for name, count in tech_counter.most_common(6)]
    
    context = {
        'featured_projects': featured_projects,
        'project_metrics': project_metrics,
        'stack_snapshot': stack_snapshot,
        'specializations': specializations,
        'profile_links': {
            'github': 'https://github.com/MuthoniGathiithi',
            'linkedin': 'https://linkedin.com/in/muthoni-gathiithi',
            'hackerrank': 'https://www.hackerrank.com/profile/gathiithijoyce74',
            'tryhackme': 'https://tryhackme.com/p/MuthoniGathiithi',
        },
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page with detailed information"""
    projects = Project.objects.all()
    category_lookup = _category_lookup()
    skills = Skill.objects.all()

    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        skills_by_category.setdefault(category, []).append(skill)

    total_projects = projects.count()
    render_deployments = projects.exclude(live_demo_url__isnull=True).exclude(live_demo_url='').count()
    security_focus = projects.filter(category='security').count()

    category_breakdown = []
    category_tech = defaultdict(set)
    category_projects = defaultdict(list)

    for project in projects:
        category_breakdown.append(project.category)
        category_projects[project.category].append(project)
        for tech in _tech_stack_list(project):
            category_tech[project.category].add(tech)

    skills_insights = []
    for key, label in Project.CATEGORY_CHOICES:
        if not category_projects.get(key):
            continue
        skills_insights.append(
            {
                'label': label,
                'count': len(category_projects[key]),
                'tech_stack': sorted(category_tech[key])[:6],
                'projects': [proj.title for proj in category_projects[key][:3]],
            }
        )

    tech_counter = Counter()
    for project in projects:
        tech_counter.update(_tech_stack_list(project))

    impact_metrics = [
        {'label': 'Deployed Platforms', 'value': render_deployments, 'caption': 'Render-secured Django apps'},
        {'label': 'GitHub Repositories', 'value': total_projects, 'caption': 'All open-source and documented'},
        {'label': 'Security & AI Tools', 'value': security_focus, 'caption': 'Automation & detection systems'},
    ]

    context = {
        'skills_by_category': skills_by_category,
        'skills_insights': skills_insights,
        'impact_metrics': impact_metrics,
        'project_story': {
            'total': total_projects,
            'categories': [
                {'label': category_lookup.get(key, key), 'count': len(category_projects.get(key, []))}
                for key, _ in Project.CATEGORY_CHOICES
                if category_projects.get(key)
            ],
            'top_stack': [{'name': name, 'count': count} for name, count in tech_counter.most_common(8)],
        },
        'profile_links': {
            'github': 'https://github.com/MuthoniGathiithi',
            'linkedin': 'https://linkedin.com/in/muthoni-gathiithi',
            'hackerrank': 'https://www.hackerrank.com/profile/gathiithijoyce74',
            'tryhackme': 'https://tryhackme.com/p/MuthoniGathiithi',
            'email': 'mailto:gathiithijoyce74@gmail.com',
        },
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects page with filtering and pagination"""
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        projects_list = Project.objects.all()
    else:
        projects_list = Project.objects.filter(category=category)
    
    categories = Project.CATEGORY_CHOICES
    
    context = {
        'projects': projects_list,
        'categories': categories,
        'current_category': category,
        'project_total': projects_list.count(),
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
