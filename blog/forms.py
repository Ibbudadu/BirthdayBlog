from django import forms
from .models import BirthdayWish

class BirthdayWishForm(forms.ModelForm):
    class Meta:
        model = BirthdayWish
        fields = ['name', 'message']
