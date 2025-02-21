from django.urls import path
from .views import CompanyList, CompanyCreate, CompanyDetail, CompanyUpdate, CompanyPatch, CompanyDelete, EmployeeList, EmployeeCreate, EmployeeDetail, EmployeeUpdate, EmployeePatch, EmployeeDelete
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('companies/', CompanyList.as_view(), name='companies_list'),
    path('company/<int:pk>', CompanyDetail.as_view(), name='company-detail'),
    path('company_create/', CompanyCreate.as_view(), name='company-create'),
    path('company_update/<int:pk>/', CompanyUpdate.as_view(), name='company-update'),
    path('company_patch/<int:pk>/', CompanyPatch.as_view(), name='company-patch'),
    path('company_delete/<int:pk>/', CompanyDelete.as_view(), name='company-delete'),

    path('employees/', EmployeeList.as_view(), name='employees_list'),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee-detail'),
    path('employee_create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employee_update/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee_patch/<int:pk>/', EmployeePatch.as_view(), name='employee-patch'),
    path('employee_delete/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete')
]


















 
        
