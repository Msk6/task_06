from .models import Restaurant
from django import forms

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'opening_time', 'closing_time']