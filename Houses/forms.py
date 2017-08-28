from django import forms
from django.forms import ModelForm, Textarea
from Houses.models import Address
from Houses.models import Customer


class CustomerForm(ModelForm):

    fields_map = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email',
        'contact_number': 'Contact Number',
    }

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'contact_number']

    def add_prefix(self, field_name):
        field_name = self.fields_map.get(field_name, field_name)
        return super(CustomerForm, self).add_prefix(field_name)


class AddressFrom(ModelForm):
    class Meta:
        model = Address
        fields = ['unit', 'street_no', 'street', 'street2', 'state', 'postal_code']
