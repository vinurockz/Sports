from django import forms
from Sportsadmin.models import MyUser
from Sportsadmin.admin import UserCreationForm

class Reg_Form(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["user_name","email","phone_number","wallet_amount","password1","password2"]

class Log_Form(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

