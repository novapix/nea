from django.core.management.base import BaseCommand
from billing.models import NepaliMonth


class Command(BaseCommand):
    help = 'Seed NepaliMonth table with months and their Nepali names'

    def handle(self, *args, **kwargs):
        months = [
            {'month_number': 1, 'name_en': 'Baisakh', 'name_np': 'वैशाख'},
            {'month_number': 2, 'name_en': 'Jestha', 'name_np': 'जेठ'},
            {'month_number': 3, 'name_en': 'Ashadh', 'name_np': 'असार'},
            {'month_number': 4, 'name_en': 'Shrawan', 'name_np': 'श्रावण'},
            {'month_number': 5, 'name_en': 'Bhadra', 'name_np': 'भाद्र'},
            {'month_number': 6, 'name_en': 'Ashwin', 'name_np': 'आश्विन'},
            {'month_number': 7, 'name_en': 'Kartik', 'name_np': 'कार्तिक'},
            {'month_number': 8, 'name_en': 'Mangsir', 'name_np': 'मंसिर'},
            {'month_number': 9, 'name_en': 'Poush', 'name_np': 'पौष'},
            {'month_number': 10, 'name_en': 'Magh', 'name_np': 'माघ'},
            {'month_number': 11, 'name_en': 'Falgun', 'name_np': 'फाल्गुन'},
            {'month_number': 12, 'name_en': 'Chaitra', 'name_np': 'चैत्र'},
        ]

        for month in months:
            obj, created = NepaliMonth.objects.get_or_create(
                month_number=month['month_number'],
                defaults={
                    'name_en': month['name_en'],
                    'name_np': month['name_np'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created month: {obj}"))
            else:
                self.stdout.write(f"Month already exists: {obj}")
