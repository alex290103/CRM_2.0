from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from users.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(validators=[RegexValidator('(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{8,}')], widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('f_name','l_name','email','telephone','password1','password2')

class LoginForm(AuthenticationForm):
    #email = forms.EmailField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput)
