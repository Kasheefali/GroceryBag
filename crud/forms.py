from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product



class DateInput(forms.DateInput):
	input_type = 'date'


class ProductForm(forms.ModelForm):
	"""docstring for OrderForm"""
	class Meta:
		model = Product
		fields = '__all__'

		widgets = {
         'item_name': forms.TextInput(attrs={
                              'style': 'height: 35px; width:1110px','placeholder':'  Item Name '}),
         'item_quantity': forms.TextInput(attrs={
                              'style': 'height: 35px; width:1110px','placeholder':'  Item Quantity '}),
         'item_status': forms.Select(attrs={
                              'style': 'height: 35px; width:1110px'}),
         'date_created': DateInput(attrs={
                              'style': 'height: 35px; width:1110px'}),
         

       }


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

