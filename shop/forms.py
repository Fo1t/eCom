from django import forms
from .models import Product
from shop.models import Category


class LoginForm(forms.Form):
    username = forms.CharField()
    username.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'Email'})
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'input100', 'name': 'pass', 'placeholder': 'Password'})

class EditForm(forms.Form):
    price = forms.FloatField(min_value=0.01)
    description = forms.CharField(widget=forms.Textarea, max_length=5000)
    discounted_price = forms.FloatField(min_value=0.01)
    #sale = forms.FloatField(max_value=100)
    title = forms.CharField(max_length=255)
    category = forms.MultipleChoiceField(choices=[(item.id, item.title) for item in Category.objects.all()])
    weight = forms.FloatField(min_value=0.0)
    file = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

class SearchForm(forms.Form):
    input = forms.CharField(max_length=100)
    input.widget.attrs.update({'type': '"text"', 'placeholder': '"Что вам нужно?"'})

class SideBarForm(forms.Form):
    minamount = forms.CharField()
    maxamount = forms.CharField()
    minamount.widget.attrs.update({'id': 'minamount', 'type': 'text'})
    maxamount.widget.attrs.update({'id': 'maxamount', 'type': 'text'})
# title = models.CharField(max_length=255)
#     description = models.TextField(max_length=10000)
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
#     price = models.FloatField(null=True)
#     created_date = models.DateTimeField(default=timezone.now)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     AVAILABILITY_STATUS = (
#         ('i', 'In Stock'),
#         ('s', 'Available at short notice'),
#         ('o', 'Ordered on demand'),
#         ('n', 'Not available'),
#     )
#     availability = models.CharField(max_length=1, choices=AVAILABILITY_STATUS, blank=True, default='n')
#     weight = models.FloatField(null=True)
#     sale = models.FloatField(null=True, default=0.0)
#     discounted_price = models.FloatField(null=True, default=0.0)