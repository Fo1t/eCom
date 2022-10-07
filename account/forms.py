from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True)
    first_name.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'first_name'})
    last_name = forms.CharField(max_length=150, required=True)
    last_name.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'last_name'})
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'input100', 'name': 'pass', 'placeholder': 'Password'})
    email = forms.EmailField(required=True)
    email.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'Email'})
    city = forms.CharField(max_length=100, required=False)
    city.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'city'})
    address = forms.CharField(max_length=100, required=False)
    address.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'address'})
    post_code = forms.IntegerField(max_value=999999, min_value=100000, required=False)
    post_code.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'post_code'})
    phone = forms.IntegerField(required=True)
    phone.widget.attrs.update({'class': 'input100', 'type': 'text', 'name': 'email', 'placeholder': 'phone'})