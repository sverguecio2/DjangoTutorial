from django.urls import path
from . import views  # Importo las vistas de myapp

urlpatterns = [
    path('', views.index, name='index'),  # Agrego la vista index
    path('hello/<str:username>', views.hello, name='hello'),  # Agrego la vista hello
    path('about/', views.about, name='about'),  # Agrego la vista about
    path('projects/', views.projects, name='projects'),  # Agrego la vista projects
    path('tasks/', views.tasks, name='tasks'),  # Agrego la vista tasks
    path('create_task/', views.create_task, name='create_task'),  # Agrego la vista create_task
    path('create_project/', views.create_project, name='create_project'),  # Agrego la vista create_project
]
