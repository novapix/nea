from django.core.management.base import BaseCommand
from billing.models import Role, EmployeeType

class Command(BaseCommand):
    help = 'Seed initial roles and employee types'

    def handle(self, *args, **kwargs):
        # Seed roles
        roles = [
            {'name': 'employee', 'status': True},
            {'name': 'customer', 'status': True},
        ]
        
        for role_data in roles:
            Role.objects.get_or_create(
                name=role_data['name'],
                defaults={'status': role_data['status']}
            )
        
        # Seed employee types
        employee_types = [
            {'name': 'superadmin', 'status': True},
            {'name': 'branch_admin', 'status': True},
            {'name': 'meter_reader', 'status': True},
        ]
        
        for type_data in employee_types:
            EmployeeType.objects.get_or_create(
                name=type_data['name'],
                defaults={'status': type_data['status']}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded roles and employee types'))
