from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from billing.models import User, Employee, Role, EmployeeType, Branch

class Command(BaseCommand):
    help = 'Seed initial master admin with employee and user account'

    def handle(self, *args, **kwargs):
        # Get or create required roles and types
        role, _ = Role.objects.get_or_create(name='superadmin')
        emp_type, _ = EmployeeType.objects.get_or_create(name='superadmin')
        branch, _ = Branch.objects.get_or_create(branch_code='HO')

        # Create master admin user
        user, user_created = User.objects.get_or_create(
            username='masteradmin',
            defaults={
                'email': input("Enter email: ").strip(),
                'password': make_password(input("Enter password: ")),
                'status': True,
                'role': role,
                'profile_picture': 'https://imgv2-1-f.scribdassets.com/img/document/773273642/original/992887a4dc/1?v=1',
            }
        )

        # Create corresponding employee
        employee, emp_created = Employee.objects.get_or_create(
            name='Master Administrator',
            defaults={
                'employee_type': emp_type,
                'branch': branch,
                'status': True,
                'user': user,
                'employee_code': 'MA',
                'contact_no': '977-1-4153051',
                'citizenship_no': '123456789',
                'citizenship_file_location': 'https://imgv2-1-f.scribdassets.com/img/document/773273642/original/992887a4dc/1?v=1',
                'address': 'Kathmandu',
            }
        )

        if user_created or emp_created:
            self.stdout.write(self.style.SUCCESS('Successfully created master admin'))
        else:
            self.stdout.write(self.style.SUCCESS('Master admin already exists'))
