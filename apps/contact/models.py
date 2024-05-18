from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Contact(models.Model):
    TITLE_CHOICES = [
        ('Менеджер', 'Менеджер'),
        ('Директор', 'Директор'),
        ('Представитель', 'Представитель'),
        ('Другой', 'Другой'),
    ]
    DEPARTMENT_CHOICES = [
        ('Продажи', 'Продажи'),
        ('Маркетинг', 'Маркетинг'),
        ('IT', 'IT'),
        ('Финансы', 'Финансы'),
        ('HR', 'HR'),
        ('Другое', 'Другое'),
    ]
    PREFERRED_COMMUNICATION_CHOICES = [
        ('Электронная почта', 'Электронная почта'),
        ('Телефон', 'Телефон'),
        ('Текст', 'Текст'),
        ('Лично', 'Лично'),
    ]
    first_name = models.CharField(max_length=50, default='', verbose_name='Имя')
    last_name = models.CharField(max_length=50, default='', verbose_name='Фамилия')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    title = models.CharField(max_length=50, choices=TITLE_CHOICES, null=True, blank=True,
                             verbose_name='Должность')
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True, blank=True,
                                  verbose_name='Отдел')
    business_partner = models.ForeignKey('business_partner.BusinessPartner', on_delete=models.CASCADE,
                                         related_name='contacts', null=True, blank=True,
                                         verbose_name='Контрагент')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
    notes = models.TextField(null=True, blank=True, verbose_name='Примечания')
    last_contacted = models.DateField(default=date.today, verbose_name='Последнее взаимодействие')
    preferred_communication = models.CharField(max_length=50,
                                               choices=PREFERRED_COMMUNICATION_CHOICES, null=True,
                                               blank=True, verbose_name='Предпочтительный способ связи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='Пользователь')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



