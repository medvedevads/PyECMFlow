from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    assign_to_me = forms.BooleanField(required=False, label='Назначить на меня')

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'title', 'department',
                  'business_partner', 'address', 'notes', 'last_contacted',
                  'preferred_communication', 'user']
