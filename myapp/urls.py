from django.urls import path
from . import views


urlpatterns = [
    path("",views.index_page, name='home'),
    path("about/",views.about,name='about'),
    path("projects/",views.projects,name='project'),
    path("project/create",views.create_project,name='create_project'),
    path("tasks/",views.tasks,name='task'),
    path("tasks/create",views.create_task,name='create_task'),
    path("tasks/update/<int:id>",views.task_update,name='task_update'),
    path("tasks/delete/<int:id>",views.task_delete,name='task_delete'),
    path("project/project_detail/<int:id>",views.project_detail,name='project_detail')
]
