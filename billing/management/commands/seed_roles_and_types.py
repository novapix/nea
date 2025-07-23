from django.core.management.base import BaseCommand
from billing.models import Role

class Command(BaseCommand):
    help = 'Seed initial roles'

    def handle(self, *args, **kwargs):
        # Seed roles
        roles = [
            {'name': 'superadmin', 'status': True},
            {'name': 'customer', 'status': True},
            {'name': 'branch_admin', 'status': True},
            {'name': 'meter_reader', 'status': True},
        ]
        
        for role_data in roles:
            Role.objects.get_or_create(
                name=role_data['name'],
                defaults={'status': role_data['status']}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded roles'))
