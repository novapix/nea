from django.shortcuts import redirect
from django.urls import reverse

def get_dashboard_redirect_by_role(profile):
    """
    Returns the dashboard redirect name based on the user's role.
    """
    role_name = profile.role.name.lower()
    if role_name == 'superadmin':
        return 'superadmin_dashboard'
    elif role_name == 'branch_admin':
        return 'branch_admin_dashboard'
    elif role_name == 'meter_reader':
        return 'meter_reader_dashboard'
    elif role_name == 'customer':
        return 'customer_dashboard'
    return None

def get_role_redirect(user):
    """
    Returns the appropriate redirect response based on user's role
    """
    if not user.role:
        return None
        
    role_name = user.role.name.lower()
    
    redirect_map = {
        'superadmin': 'superadmin_dashboard',
        'branch_admin': 'branch_admin_dashboard',
        'meter_reader': 'meter_reader_dashboard',
        'customer': 'customer_dashboard'
    }
    
    return redirect_map.get(role_name, 'branch_list')
