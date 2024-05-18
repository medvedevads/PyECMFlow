import random
from random import choice
from faker import Faker
from django.core.management.base import BaseCommand
from apps.contracts.models import Contracts
from apps.business_partner.models import BusinessPartner


class Command(BaseCommand):
    help = 'Generate fake contracts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Contract id')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker()
        currency = ['RUB', 'EUR', 'USD', 'CNY', 'GBP', 'CHF']
        role = ['Архив', 'Заблокирован','Проверен']
        categories = ['Агентский договор', 'Договор аренды', 'Договор возмездного оказания услуг',
                      'Договор купли - продажи''Договор пожертвования', 'Договор поставки','Договор займа']
        business_partners=BusinessPartner.objects.all()


        for i in range(1, count + 1):
            contract = Contracts(
                name=f'Договор {i}',
                date=fake.date_between(start_date='-1y', end_date='today'),
                reg_number=random.randint(1000000000, 9999999999),
                content=f'Краткое содержание договора {i}',
                business_partner=choice(business_partners),
                country=f'Россия',
                contract_currency=choice(currency),
                validity=choice(role),
                due_to=fake.date_between(start_date='today', end_date='+1y'),
                category=choice(categories),
            )
            contract.save()
