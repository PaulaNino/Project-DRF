from django.urls import path
from .views import DepartmentList, DepartmentCreate, DepartmentDetail, DepartmentUpdate, DepartmentPatch, DepartmentDelete
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('departments/', DepartmentList.as_view(), name='departments_list'),
    path('department/<int:pk>', DepartmentDetail.as_view(), name='department-detail'),
    path('department_create/', DepartmentCreate.as_view(), name='department-create'),
    path('department_update/<int:pk>/', DepartmentUpdate.as_view(), name='department-update'),
    path('department_patch/<int:pk>/', DepartmentPatch.as_view(), name='department-patch'),
    path('department_delete/<int:pk>/', DepartmentDelete.as_view(), name='department-delete'),
]