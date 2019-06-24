"""raptor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from project.views import (
    index_view, project_view, create_new_project_view, project_modify_view
)

app_name = 'project'

urlpatterns = [
    path("", index_view),
    path('Admin/', admin.site.urls),
    path('Documentation/', admin.site.urls),
    path('Documentation/tools/Bep-Bundle', admin.site.urls),
    path('Documentation/tools/Raptor-Cli', admin.site.urls),
    path('Documentation/tools/Raptor-Cli/REST-api', admin.site.urls),
    path('Documentation/tools/Bep-Step', admin.site.urls),
    path('Documentation/tools/Null-Catcher', admin.site.urls),
    path('Documentation/tools/Clean-Machine', admin.site.urls),
    path('Documentation/tools/', admin.site.urls),
    path('Documentation/Setup/', admin.site.urls),
    path('Documentation/Celery/', admin.site.urls),
    path('Documentation/Login/', admin.site.urls),
    path('Projects/', project_view),
    path('Projects/CreateNew', create_new_project_view),
    path('Projects/<str:project_id>', admin.site.urls),
    path('Projects/<str:project_id>/ModifyProject', project_modify_view),
    path('Projects/<str:project_id>/<str:build_id>', admin.site.urls),
    path('Projects/<str:project_id>/<str:build_id>/Update', admin.site.urls),
    path('Projects/<str:project_id>/<str:build_id>/Stats', admin.site.urls),
    path('FAQ/', admin.site.urls),
    path('Previous-Results/', admin.site.urls),
    path('Git/', admin.site.urls),
]
