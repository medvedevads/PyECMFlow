from random import choice
from faker import Faker
from django.core.management.base import BaseCommand
from apps.tasks.models import Task


class Command(BaseCommand):
    help = 'Generate fake contracts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Contract id')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker()
        status = ['Выполнить', 'В процессе', 'Завершено', 'Отменено']

        for i in range(1, count + 1):
            contract = Task(
                title=f'Задание {i}',
                description=f'Описание задания {i}',
                status=choice(status),
                due_date=fake.date_between(start_date='today', end_date='+1y'),
            )
            contract.save()
