from django.urls import path
from .views import (
    LoginView, logout_view,
    BranchListView, BranchCreateView, BranchUpdateView, toggle_branch_status, superadmin_dashboard
)

app_name = 'billing'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('branches/', BranchListView.as_view(), name='branch_list'),
    path('branches/add/', BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:pk>/edit/', BranchUpdateView.as_view(), name='branch_update'),
    path('branches/<int:pk>/toggle-status/', toggle_branch_status, name='toggle_branch_status'),
    path('admin/', superadmin_dashboard, name='superadmin_dashboard'),
]
