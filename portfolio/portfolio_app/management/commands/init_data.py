from portfolio_app.models import Project, Contact
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Init data'

    def handle(self, *args, **kwargs):
        # Adding projects to database
        proj = Project.objects.get_or_create(name='Test project', description='The best project ever!')
        proj = Project.objects.get_or_create(name='Test project 2', description='The best project ever2!', link="https://vk.com")

        #adding contacts to database
        cont = Contact.objects.get_or_create(name='Telegram', link="https://t.me/yeawouu")
        cont = Contact.objects.get_or_create(name='VK')
        cont = Contact.objects.get_or_create(name="GitHub", link="https://github.com/SokolOFFF")