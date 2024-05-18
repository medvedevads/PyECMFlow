# Generated by Django 5.0.4 on 2024-05-12 19:00

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_partner', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(default='', max_length=200, verbose_name='Регистрационный номер')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата заключения')),
                ('content', models.CharField(default='', max_length=100, verbose_name='Содержание')),
                ('country', models.CharField(default='', max_length=100, verbose_name='Страна')),
                ('contract_currency', models.CharField(default='', max_length=100, verbose_name='Валюта контракта')),
                ('validity', models.CharField(default='', max_length=100, verbose_name='Статус')),
                ('due_to', models.DateField(null=True, verbose_name='Дата окончания действия')),
                ('category', models.CharField(default='', max_length=200, verbose_name='Категория')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('contract_file', models.FileField(blank=True, null=True, upload_to='contract_files/', verbose_name='Договор')),
                ('business_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='business_partner.businesspartner', verbose_name='Контрагент')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
