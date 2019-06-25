from django.contrib import admin

# Register your models here.
from .models import Project, Build, Results

admin.site.register(Project)
admin.site.register(Build)
admin.site.register(Results)