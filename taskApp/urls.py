from django.urls import path
from .views import login, logout, register, project_list, add_project, task_list, profile, personnel, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('projects/', project_list, name='projects'),
    path('projects/add/', add_project, name='add_project'),
    path('projects/<int:project_id>/tasks/', task_list, name='tasks'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('personnel/', personnel, name='personnel'),
]
