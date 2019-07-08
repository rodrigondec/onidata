from django.core.management import BaseCommand

from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crate super user'

    def handle(self, *args, **options):
        model = get_user_model()
        if not model.objects.filter(email='superadmin@admin.com'):
            superuser = model(username='superuser', email='superuser@admin.com',
                              is_staff=True, is_superuser=True)
            superuser.save()
            superuser.set_password('@Admin123')
            superuser.save()
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write(self.style.ERROR('Superuser already created!'))
