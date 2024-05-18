from django.db import models
from django.contrib.auth.models import User

class BusinessPartner(models.Model):

    INDUSTRY_CHOICES = [
        ('Производство', 'Производство'),
        ('Розничная торговля', 'Розничная торговля'),
        ('Здравоохранение', 'Здравоохранение'),
        ('IT', 'IT'),
        ('Финансы', 'Финансы'),
        ('Образование', 'Образование'),
        ('Строительство', 'Строительство'),
        ('Транспорт', 'Транспорт'),
        ('Сельское хозяйство', 'Сельское хозяйство'),
        ('Энергетика', 'Энергетика'),
        ('Банк', 'Банк'),
    ]


    PRIMARY_ROLE_CHOICES = [
        ('покупатель', 'Покупатель'),
        ('поставщик', 'Поставщик'),
        ('партнер', 'Партнер'),
        ('Банк', 'Банк'),
    ]


    SECONDARY_ROLE_CHOICES = [
        ('покупатель', 'Покупатель'),
        ('поставщик', 'Поставщик'),
        ('партнер', 'Партнер'),
        ('Банк', 'Банк'),
        ('-', '-'),
    ]


    STATUS_CHOICES = [
        ('Архив', 'Архив'),
        ('Заблокирован', 'Заблокирован'),
        ('Проверен', 'Проверен'),
    ]


    RESIDENCE_CHOICES = [
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    ]

    name = models.CharField(max_length=100, default='', verbose_name='Наименование')
    residence = models.CharField(max_length=100, default='', verbose_name='Резидент')
    vat = models.CharField(max_length=100, default='', verbose_name='Регистрационный номер')
    email = models.EmailField(max_length=100, default='', verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, default='', verbose_name='Телефон')
    country = models.CharField(max_length=100, default='', verbose_name='Страна')
    postcode = models.CharField(max_length=20, default='', verbose_name='Индекс')
    city = models.CharField(max_length=100, default='', verbose_name='Город')
    street_name = models.CharField(max_length=200, default='', verbose_name='Улица')
    house_number = models.CharField(max_length=20, default='', verbose_name='Дом')
    industry = models.CharField(max_length=200, default='', verbose_name='Вид деятельности')
    primary_role = models.CharField(max_length=100, default='', verbose_name='Роль')
    secondary_role = models.CharField(max_length=100, default='', verbose_name='Доп. роль')
    status = models.CharField(max_length=100, default='', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers',
                             null=True, verbose_name='Пользователь')


    def get_full_address(self):
        return f"{self.postcode}, {self.country}, {self.city}, {self.street_name}, {self.house_number}"

    def __str__(self):
        return self.name


