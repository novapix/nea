from django.core.management.base import BaseCommand
from billing.models import Branch

class Command(BaseCommand):
    help = 'Seed initial branches'

    def handle(self, *args, **kwargs):
        # Seed head office
        Branch.objects.get_or_create(
            branch_code='HO',
            defaults={
                'name': 'Head Office',
                'address': 'Kathmandu',
                'contact': '977-1-4153051',
                'status': True,
                'branch_incharge': None 
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded branches'))
