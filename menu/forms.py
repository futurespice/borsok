from django import forms
from .models import Category

class DishSearchForm(forms.Form):
    name = forms.CharField(label='Название блюда', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', required=False)
