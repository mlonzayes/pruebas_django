from django.contrib import admin
from .models import Task,Project

admin.site.register([
    Project,
    Task
])