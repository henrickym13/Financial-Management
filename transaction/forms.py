from django import forms
from .models import Transaction
from category.models import Category


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'date', 'type_choice', 'category']
        widgets= {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class TransactionFilterForm(forms.Form):
    start_date = forms.DateField(
        required = False,
        widget = forms.DateInput(attrs={'type': 'date'}),
        label = 'Data Inicial'
    )
    end_date = forms.DateField(
        required = False,
        widget = forms.DateInput(attrs={'type': 'date'}),
        label = 'Data Final'
    )
    type_choice = forms.ChoiceField(
        choices=[('', 'Todos')] + list(Transaction.TRANSACTION_TYPES),
        required= False,
        label = 'Tipos',
    )
    category = forms.ChoiceField(
        choices=[('', 'Todos')],
        required= False,
        label = 'Categoria',
    )