from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Customer, Branch, UserProfile, Role
from .utils import get_dashboard_redirect_by_role

def login_view(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            dashboard = get_dashboard_redirect_by_role(profile)
            if dashboard:
                return redirect(dashboard)
            else:
                messages.error(request, 'Unauthorized role.')
                return redirect('login')
        except UserProfile.DoesNotExist:
            messages.error(request, 'No user profile found.')
            return redirect('login')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    profile = UserProfile.objects.get(user=user)
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    dashboard = get_dashboard_redirect_by_role(profile)
                    if dashboard:
                        return redirect(dashboard)
                    else:
                        messages.error(request, 'Unauthorized role.')
                        return redirect('login')
                except UserProfile.DoesNotExist:
                    messages.error(request, 'No user profile found.')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form, 'hide_navbar': True})
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
