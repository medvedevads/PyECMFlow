from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from .models import BusinessPartner

class BusinessPartnerForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Пользователь')
    industry = forms.ChoiceField(choices=BusinessPartner.INDUSTRY_CHOICES, label='Вид деятельности')
    primary_role = forms.ChoiceField(choices=BusinessPartner.PRIMARY_ROLE_CHOICES, label='Роль контрагента')
    secondary_role = forms.ChoiceField(choices=BusinessPartner.SECONDARY_ROLE_CHOICES, label='Дополнительно')
    status = forms.ChoiceField(choices=BusinessPartner.STATUS_CHOICES, label='Статус')
    residence = forms.ChoiceField(choices=BusinessPartner.RESIDENCE_CHOICES, label='Резидент')
    email = forms.EmailField(validators=[EmailValidator(message='Введите корректную почту.')],
                             label='Электронный адрес')

    class Meta:
        model = BusinessPartner
        fields = ['name', 'vat', 'email', 'phone', 'country', 'postcode', 'city',
                  'street_name', 'house_number', 'industry', 'primary_role', 'secondary_role',
                  'user', 'residence', 'status']
