from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Customer, Branch

# @user_passes_test(lambda u: u.is_superuser)
def superadmin_dashboard(request):
    context = {
        'employee_count': Employee.objects.count(),
        'customer_count': Customer.objects.count(),
        'branches': Branch.objects.all()[:5],  # Show latest 5 branches
    }
    return render(request, 'dashboard/superadmin_dashboard.html', context)
