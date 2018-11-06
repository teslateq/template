from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['company_name','name_project','email_company','web_company']

admin.site.register(Project,ProjectAdmin)
