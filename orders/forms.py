from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # email = forms.EmailField()
    # email.widget.attrs.update({'values': Order.email})
    # first_name = forms.CharField()
    # first_name.widget.attrs.update({'values': Order.first_name})
    # last_name = forms.CharField()
    # last_name.widget.attrs.update({'values': Order.last_name})
    # address = forms.CharField()
    # address.widget.attrs.update({'values': Order.address})
    # postal_code = forms.IntegerField()
    # postal_code.widget.attrs.update({'values': Order.postal_code})
    # city = forms.CharField()
    # city.widget.attrs.update({'values': Order.city})
    # create_account = forms.CheckboxInput()

    class Meta:
        model = Order
    #     #first_name = forms.CharField()
    #     # last_name = forms.CharField()
    #     # email = forms.EmailField()
    #     # address = forms.CharField()
    #     # postal_code = forms.IntegerField()
    #     # city = forms.CharField()
    #     # create_account = forms.CheckboxInput()
    #     #create_account.widget.attrs.update({'id': 'acc'})
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone']