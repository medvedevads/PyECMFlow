from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from .models import Contracts


class ContractsForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Пользователь')
    contract_currency = forms.ChoiceField(choices=Contracts.CONTRACT_CURRENCY_CHOICES,
                                          label='Валюта контракта')
    validity = forms.ChoiceField(choices=Contracts.VALIDITY_ROLE_CHOICES, label='Статус')
    category = forms.ChoiceField(choices=Contracts.CATEGORY_CHOICES, label='Категория')
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        ),
        label='Дата заключения'
    )
    due_to = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        ),
        label='Дата окончания действия'
    )


    class Meta:
        model = Contracts
        fields = ['name', 'date', 'content', 'business_partner', 'country', 'contract_currency',
                  'validity', 'due_to', 'category', 'reg_number', 'user', 'contract_file']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
