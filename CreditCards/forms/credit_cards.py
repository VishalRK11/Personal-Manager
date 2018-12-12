from django import forms
from CreditCards.models import *


class AddCreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id', 'owner_id']
        widgets = {
            'card_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the card name'}),
            'name_on_card': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter your name on card'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the card number'}),
            'cvv': forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the card cvv'}),
            'expiry_date': forms.DateInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the expiry date'}),
            'card_type': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the card type'}),
        }


class UpdateCreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id', 'owner_id']
        widgets = {
            'card_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the card name'}),
            'name_on_card': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter your name on card'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the card number'}),
            'cvv': forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the card cvv'}),
            'expiry_date': forms.DateInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the expiry date'}),
            'card_type': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Enter the card type'}),
        }
