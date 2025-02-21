from django.urls import path
from .views import ProjectList, ProjectCreate, ProjectDetail, ProjectUpdate, ProjectPatch, ProjectDelete
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('projects/', ProjectList.as_view(), name='projects_list'),
    path('project/<int:pk>', ProjectDetail.as_view(), name='project-detail'),
    path('project_create/', ProjectCreate.as_view(), name='project-create'),
    path('project_update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
    path('project_patch/<int:pk>/', ProjectPatch.as_view(), name='project-patch'),
    path('project_delete/<int:pk>/', ProjectDelete.as_view(), name='project-delete'),
]