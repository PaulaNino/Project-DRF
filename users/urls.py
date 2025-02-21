from django.urls import path
from .views import UserList, UserCreate, UserDetail, UserUpdate, UserPatch, UserDelete, UserLoginView, RoleCreate
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserList.as_view(), name='users_list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('user_create/', UserCreate.as_view(), name='user-create'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('user_patch/<int:pk>/', UserPatch.as_view(), name='user-patch'),
    path('user_delete/<int:pk>/', UserDelete.as_view(), name='user-delete'),
    path('role/', RoleCreate.as_view(), name='role-create')
]