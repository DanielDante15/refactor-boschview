from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from rest_framework import routers
urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/create', UserCreate.as_view(), name='create-user'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
    path('users/projects', UserWithProjectsList.as_view(), name='user-with-projects-list'),

    

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/create', ProjectCreate.as_view(), name='create-project'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
    path('projects/users/<int:pk>', SingleProjectWithUser.as_view(), name='project-user'),
    path('projects/users/', ProjectsWithUserList.as_view(), name='project-user'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)