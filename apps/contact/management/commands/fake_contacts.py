from faker import Faker
from django.core.management.base import BaseCommand
from apps.contact.models import Contact
from apps.business_partner.models import BusinessPartner
import random
from random import choice

class Command(BaseCommand):
    help = 'Generate fake contacts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of contacts to generate')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker()
        business_partners=BusinessPartner.objects.all()
        titles = ['Менеджер', 'Директор', 'Представитель', 'Другой']
        departments = ['Продажи', 'Маркетинг', 'IT', 'Финансы', 'HR', 'Другое']
        prefers = ['Электронная почта', 'Телефон', 'Текст', 'Лично']

        for i in range(1, count + 1):
            contact = Contact(
                # city=random.choice(cities),
                first_name=f'Имя {i}',
                last_name=f'Фамилия {i}',
                email=f'mail{i}@mail.ru',
                phone=random.randint(79000000000, 79999999999),
                title=random.choice(titles),
                department=random.choice(departments),
                business_partner=choice(business_partners),
                address=fake.address(),
                notes=f'Информация по контакту {i}',
                last_contacted=fake.date_between(start_date='-1y', end_date='today'),
                preferred_communication=random.choice(prefers),
                user=None
            )
            contact.save()