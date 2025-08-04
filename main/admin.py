from django.contrib import admin
from .models import Project, Skill, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'created_date']
    list_filter = ['category', 'featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured']
    ordering = ['-created_date']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date']
    list_filter = ['created_date']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_date']
    ordering = ['-created_date']
