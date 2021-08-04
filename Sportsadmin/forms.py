from django import forms
from django.forms import ModelForm
from .models import Sports_Catagory_Model,Item_Creation_Model,Product_Model,MyUser
from .admin import UserCreationForm


class CreateSportItems_Form(forms.ModelForm):
    class Meta:
        model=Item_Creation_Model
        fields="__all__"

class SportsCategory_Form(forms.ModelForm):
    class Meta:
        model=Sports_Catagory_Model
        fields = "__all__"

class ProductName_Form(forms.ModelForm):
    class Meta:
        model=Product_Model
        fields = "__all__"

class Reg_Form(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["user_name","email","phone_number","wallet_amount","password1","password2"]


class Log_Form(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

