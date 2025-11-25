from collections import Counter, defaultdict

from .models import Project


def project_counts(request):
    """Expose project totals and category counts to every template."""
    projects = list(Project.objects.all())
    total_projects = len(projects)
    render_deployments = sum(1 for project in projects if project.live_demo_url)

    category_map = {key: label for key, label in Project.CATEGORY_CHOICES}
    category_totals = defaultdict(list)
    tech_counter = Counter()

    for project in projects:
        category_totals[project.category].append(project)
        for tech in [tech.strip() for tech in project.technologies.split(',') if tech.strip()]:
            tech_counter[tech] += 1

    categories = []
    for key, label in Project.CATEGORY_CHOICES:
        categories.append(
            {
                'key': key,
                'label': label,
                'count': len(category_totals.get(key, [])),
            }
        )

    top_stack = [{'name': name, 'count': count} for name, count in tech_counter.most_common(6)]

    return {
        'project_counts': {
            'total': total_projects,
            'deployed': render_deployments,
            'categories': categories,
            'top_stack': top_stack,
        }
    }

