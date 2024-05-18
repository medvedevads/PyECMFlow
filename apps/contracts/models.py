from django.db import models
from apps.business_partner.models import BusinessPartner
from datetime import date
from apps.accounts.models import User


class Contracts(models.Model):
    CONTRACT_CURRENCY_CHOICES = [
        ('rub', 'RUB'),
        ('eur', 'EUR'),
        ('usd', 'USD'),
        ('cny', 'CNY'),
        ('gbp', 'GBP'),
        ('chf', 'CHF'),
    ]

    VALIDITY_ROLE_CHOICES = [
        ('Архив', 'Архив'),
        ('Заблокирован', 'Заблокирован'),
        ('Проверен', 'Проверен'),
    ]

    CATEGORY_CHOICES = [
        ('Агентский договор', 'Агентский договор'),
        ('Договор аренды', 'Договор аренды'),
        ('Договор возмездного оказания услуг', 'Договор возмездного оказания услуг'),
        ('Договор купли - продажи', 'Договор купли - продажи'),
        ('Договор пожертвования', 'Договор пожертвования'),
        ('Договор поставки', 'Договор поставки'),
        ('Договор займа', 'Договор займа'),
    ]

    reg_number = models.CharField(max_length=200, default='', verbose_name='Регистрационный номер')
    name = models.CharField(max_length=100, default='', verbose_name='Наименование')
    date = models.DateField(default=date.today, verbose_name='Дата заключения')
    content = models.CharField(max_length=100, default='', verbose_name='Содержание')
    business_partner = models.ForeignKey(BusinessPartner, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='contracts', verbose_name='Контрагент')
    country = models.CharField(max_length=100, default='', verbose_name='Страна')
    contract_currency = models.CharField(max_length=100, default='', verbose_name='Валюта контракта')
    validity = models.CharField(max_length=100, default='', verbose_name='Статус')
    due_to = models.DateField(null=True, verbose_name='Дата окончания действия')
    category = models.CharField(max_length=200, default='', verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person', null=True,
                             verbose_name='Пользователь')
    contract_file = models.FileField(upload_to='contract_files/', null=True, blank=True,
                                     verbose_name='Договор')


    def get_full_address(self):
        return f"{self.country}"

    def __str__(self):
        return self.name
