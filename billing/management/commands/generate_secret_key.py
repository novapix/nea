from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
from pathlib import Path

class Command(BaseCommand):
    help = 'Generates a new SECRET_KEY and writes it to the .env file'

    def handle(self, *args, **kwargs):
        secret_key = get_random_secret_key()
        env_path = Path(".env")

        if not env_path.exists():
            env_path.write_text(f'SECRET_KEY="{secret_key}"\n')
            self.stdout.write(self.style.SUCCESS(".env file created with SECRET_KEY."))
        else:
            lines = env_path.read_text().splitlines()
            key_exists = any(line.startswith("SECRET_KEY=") for line in lines)

            if key_exists:
                lines = [f'SECRET_KEY="{secret_key}"' if line.startswith("SECRET_KEY=") else line for line in lines]
            else:
                lines.append(f'SECRET_KEY="{secret_key}"')

            env_path.write_text("\n".join(lines) + "\n")
            self.stdout.write(self.style.SUCCESS("SECRET_KEY updated in .env file."))
