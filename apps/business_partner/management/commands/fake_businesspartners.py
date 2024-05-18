import random
from random import choice
from django.core.management.base import BaseCommand
from apps.business_partner.models import BusinessPartner


class Command(BaseCommand):
    help = 'Generate fake BP'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='BP id')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        cities = ['Москва', 'Санкт-Петербург', 'Омск', 'Калининград', 'Владивосток']
        industries = ['Производство', 'Здравоохранение', 'Финансы']
        roles = ['Покупатель', 'Поставщик', 'Партнер', 'Банк']
        s_roles = ['Покупатель', 'Поставщик', 'Партнер', '-']
        y_n = ['Да', 'Нет']
        statuses = ['Архив', 'Заблокирован', 'Проверен']

        for i in range(1, count + 1):
            bp = BusinessPartner(
                name=f'Бизнес-партнер {i}',
                residence=random.choice(y_n),
                vat=random.randint(1000000000, 9999999999),
                email=f'mail{i}@mail.ru',
                phone=random.randint(79000000000, 79999999999),
                country=f'Россия',
                postcode=random.randint(100000, 999999),
                city=random.choice(cities),
                street_name=f'Улица {i}',
                house_number=f'Дом №{i}',
                industry=choice(industries),
                primary_role=choice(roles),
                secondary_role=choice(s_roles),
                status=choice(statuses)
            )
            bp.save()
