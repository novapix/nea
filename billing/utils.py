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
