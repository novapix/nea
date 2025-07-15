from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import User, Employee, Customer, Branch, Role
from .utils import get_dashboard_redirect_by_role, get_role_redirect
from .forms import BranchAdminForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q

class SuperAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class BranchListView(LoginRequiredMixin, SuperAdminRequiredMixin, ListView):
    model = Branch
    template_name = 'branch/branch_list.html'
    context_object_name = 'branches'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        status_filter = self.request.GET.get('status')
        
        if search_query:
            queryset = queryset.filter(
                Q(branch_code__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(address__icontains=search_query)
            )
            
        if status_filter:
            queryset = queryset.filter(status=status_filter.lower() == 'active')
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['status_filter'] = self.request.GET.get('status', '')
        return context

class BranchCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = Branch
    form_class = BranchAdminForm
    template_name = 'branch/branch_form.html'
    success_url = '/branches/'

class BranchUpdateView(LoginRequiredMixin, SuperAdminRequiredMixin, UpdateView):
    model = Branch
    form_class = BranchAdminForm
    template_name = 'branch/branch_form.html'
    success_url = '/branches/'

@login_required
def toggle_branch_status(request, pk):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    try:
        branch = Branch.objects.get(pk=pk)
        branch.status = not branch.status
        branch.save()
        return JsonResponse({
            'success': True,
            'new_status': branch.status,
            'status_display': 'Active' if branch.status else 'Inactive'
        })
    except Branch.DoesNotExist:
        return JsonResponse({'error': 'Branch not found'}, status=404)

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                dashboard = get_dashboard_redirect_by_role(profile)
                if dashboard:
                    return redirect(dashboard)
                messages.error(request, 'Your role does not have access permissions')
                return redirect('login')
            except UserProfile.DoesNotExist:
                messages.error(request, 'Your account is missing required profile information')
                return redirect('login')
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid username or password')
            return render(request, 'auth/login.html')
            
        if not user.status:
            messages.error(request, 'Account pending approval')
            return render(request, 'auth/login.html')
            
        login(request, user)
        
        if not user.role:
            messages.error(request, 'Your account is missing required role information')
            return redirect('login')
            
        redirect_name = get_role_redirect(user)
        return redirect(redirect_name)

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out.')
    return redirect('login')

@login_required
def superadmin_dashboard(request):
    context = {
        'employee_count': Employee.objects.count(),
        'customer_count': Customer.objects.count(),
        'branches': Branch.objects.all()[:5],  # Show latest 5 branches
    }
    return render(request, 'dashboard/superadmin_dashboard.html', context)

@login_required
def branch_admin_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    branch = None
    employees = []
    if profile.employee:
        branch = profile.employee.branch
        employees = Employee.objects.filter(branch=branch)
    context = {
        'branch': branch,
        'employees': employees,
    }
    return render(request, 'dashboard/branch_admin_dashboard.html', context)

@login_required
def customer_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    customer = profile.customer
    context = {
        'customer': customer,
        'demand_type': customer.demand_type if customer else None,
    }
    return render(request, 'dashboard/customer_dashboard.html', context)

@login_required
def meter_reader_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    branch = None
    customers = []
    if profile.employee:
        branch = profile.employee.branch
        customers = Customer.objects.filter(branch=branch)
    context = {
        'branch': branch,
        'customers': customers,
    }
    return render(request, 'dashboard/meter_reader_dashboard.html', context)
