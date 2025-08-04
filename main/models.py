from django.db import models
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('django', 'Django Web Applications'),
        ('security', 'Cybersecurity Projects'),
        ('educational', 'Educational Content'),
        ('cpp', 'C++ Projects'),
        ('python', 'Python Scripts'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    github_url = models.URLField()
    live_demo_url = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('backend', 'Backend Development'),
        ('frontend', 'Frontend Development'),
        ('security', 'Cybersecurity'),
        ('programming', 'Programming Languages'),
        ('tools', 'Tools & Platforms'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(default=80)  # Percentage
    icon_class = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
